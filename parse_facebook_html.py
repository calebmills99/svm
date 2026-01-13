#!/usr/bin/env python3
"""
Facebook HTML Parser

Specialized parser for Facebook data export HTML files.
Extracts security-relevant information from HTML files.

Usage:
    from parse_facebook_html import FacebookHTMLParser
    parser = FacebookHTMLParser('path/to/file.html')
    data = parser.parse()
"""

from pathlib import Path
from typing import Dict, List, Any, Optional
import re

# Try to import BeautifulSoup for robust HTML parsing
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


class FacebookHTMLParser:
    """Parser for Facebook HTML export files."""
    
    def __init__(self, html_file: str):
        """Initialize parser with HTML file path."""
        self.html_file = Path(html_file)
        self.content = ""
        self.soup: Optional['BeautifulSoup'] = None
        self.data = {}
        
        if self.html_file.exists():
            with open(self.html_file, 'r', encoding='utf-8') as f:
                self.content = f.read()
            
            # Parse with BeautifulSoup if available
            if HAS_BS4 and self.content:
                self.soup = BeautifulSoup(self.content, 'lxml')
    
    def extract_login_history(self) -> List[Dict[str, Any]]:
        """Extract login history from security HTML files."""
        logins = []
        
        # Common patterns in Facebook's security HTML
        patterns = [
            r'IP[:\s]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
            r'(?:Location|City)[:\s]+([^<\n]+)',
            r'(?:Device|Browser)[:\s]+([^<\n]+)',
            r'(?:Time|Date)[:\s]+([^<\n]+)',
        ]
        
        # Extract IP addresses
        ips = re.findall(patterns[0], self.content)
        
        # Extract locations
        locations = re.findall(patterns[1], self.content)
        
        # Extract devices
        devices = re.findall(patterns[2], self.content)
        
        # Extract timestamps
        timestamps = re.findall(patterns[3], self.content)
        
        # Combine into login records
        lengths = [len(ips), len(locations), len(devices), len(timestamps)]
        max_len = max(lengths) if any(lengths) else 0
        
        for i in range(max_len):
            login = {
                'ip': ips[i] if i < len(ips) else None,
                'location': locations[i].strip() if i < len(locations) else None,
                'device': devices[i].strip() if i < len(devices) else None,
                'timestamp': timestamps[i].strip() if i < len(timestamps) else None,
                'source_file': self.html_file.name
            }
            logins.append(login)
        
        return logins
    
    def extract_security_events(self) -> List[Dict[str, Any]]:
        """Extract security-related events from HTML."""
        events = []
        
        # Keywords that indicate security events
        security_keywords = [
            'password changed',
            'password reset',
            'email changed',
            'phone number added',
            'phone number removed',
            'two-factor authentication',
            'security code',
            'login alert',
            'suspicious activity',
            'unrecognized device',
            'account recovery',
            'security checkup',
        ]
        
        # Split content into lines for context
        lines = self.content.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            for keyword in security_keywords:
                if keyword in line_lower:
                    # Get context (surrounding lines)
                    context_start = max(0, i - 2)
                    context_end = min(len(lines), i + 3)
                    context = ' '.join(lines[context_start:context_end])
                    
                    # Clean HTML tags (basic cleaning)
                    context = re.sub(r'<[^>]+>', ' ', context)
                    context = re.sub(r'\s+', ' ', context).strip()
                    
                    events.append({
                        'keyword': keyword,
                        'context': context[:500],  # Limit context length
                        'line_number': i + 1,
                        'source_file': self.html_file.name
                    })
        
        return events
    
    def extract_ip_addresses(self) -> List[str]:
        """Extract all IP addresses from the HTML content."""
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ips = re.findall(ip_pattern, self.content)
        return list(set(ips))  # Return unique IPs
    
    def extract_dates(self) -> List[str]:
        """Extract dates from the HTML content."""
        date_patterns = [
            r'\d{1,2}/\d{1,2}/\d{4}',  # MM/DD/YYYY
            r'\d{4}-\d{2}-\d{2}',      # YYYY-MM-DD
            r'\d{1,2} [A-Za-z]+ \d{4}', # DD Month YYYY
            r'[A-Za-z]+ \d{1,2}, \d{4}', # Month DD, YYYY
        ]
        
        dates = []
        for pattern in date_patterns:
            dates.extend(re.findall(pattern, self.content))
        
        return dates
    
    def extract_structured_data(self) -> Dict[str, Any]:
        """Extract structured data from Facebook HTML tables."""
        data = {
            'logins': [],
            'devices': [],
            'locations': [],
            'ips': [],
            'all_rows': []
        }
        
        # Use BeautifulSoup if available for robust parsing
        if HAS_BS4 and self.soup:
            return self._extract_with_beautifulsoup(data)
        else:
            return self._extract_with_regex(data)
    
    def _extract_with_beautifulsoup(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract data using BeautifulSoup for robust HTML parsing."""
        if not self.soup:
            return data
        
        # Find all tables
        for table in self.soup.find_all('table'):
            for row in table.find_all('tr'):
                cells = row.find_all(['td', 'th'])
                cleaned_cells = [cell.get_text(strip=True) for cell in cells]
                
                if cleaned_cells and any(cell for cell in cleaned_cells):
                    row_text = ' '.join(cleaned_cells).lower()
                    data['all_rows'].append(cleaned_cells)
                    
                    # Categorize based on content
                    if any(word in row_text for word in ['login', 'session', 'logged in']):
                        data['logins'].append(cleaned_cells)
                    if 'device' in row_text or 'browser' in row_text or 'chrome' in row_text or 'safari' in row_text:
                        data['devices'].append(cleaned_cells)
                    if 'location' in row_text or 'city' in row_text:
                        data['locations'].append(cleaned_cells)
        
        # Also extract divs with security-like content (Facebook uses divs heavily)
        for div in self.soup.find_all('div'):
            text = div.get_text(strip=True)
            if len(text) > 10 and len(text) < 500:  # Reasonable text length
                text_lower = text.lower()
                if any(kw in text_lower for kw in ['ip address', 'device', 'location', 'browser', 'login']):
                    data['all_rows'].append([text])
        
        return data
    
    def _extract_with_regex(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Fallback regex-based extraction when BeautifulSoup is unavailable."""
        # Extract tables using basic pattern matching
        table_pattern = r'<table[^>]*>(.*?)</table>'
        tables = re.findall(table_pattern, self.content, re.DOTALL | re.IGNORECASE)
        
        for table in tables:
            # Extract rows
            row_pattern = r'<tr[^>]*>(.*?)</tr>'
            rows = re.findall(row_pattern, table, re.DOTALL | re.IGNORECASE)
            
            for row in rows:
                # Extract cells
                cell_pattern = r'<t[dh][^>]*>(.*?)</t[dh]>'
                cells = re.findall(cell_pattern, row, re.DOTALL | re.IGNORECASE)
                
                # Clean cell content
                cleaned_cells = []
                for cell in cells:
                    cleaned = re.sub(r'<[^>]+>', '', cell)
                    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
                    cleaned_cells.append(cleaned)
                
                # Store if we have data
                if cleaned_cells and any(cell for cell in cleaned_cells):
                    row_text = ' '.join(cleaned_cells).lower()
                    data['all_rows'].append(cleaned_cells)
                    
                    if any(word in row_text for word in ['login', 'session']):
                        data['logins'].append(cleaned_cells)
                    elif 'device' in row_text or 'browser' in row_text:
                        data['devices'].append(cleaned_cells)
                    elif 'location' in row_text or 'city' in row_text:
                        data['locations'].append(cleaned_cells)
        
        return data
    
    def parse(self) -> Dict[str, Any]:
        """Parse the HTML file and return all extracted data."""
        if not self.content:
            return {'error': 'File not found or empty'}
        
        return {
            'file': self.html_file.name,
            'login_history': self.extract_login_history(),
            'security_events': self.extract_security_events(),
            'ip_addresses': self.extract_ip_addresses(),
            'dates': self.extract_dates(),
            'structured_data': self.extract_structured_data()
        }
    
    def generate_summary(self) -> str:
        """Generate a human-readable summary of the parsed data."""
        data = self.parse()
        
        # Handle error case
        if 'error' in data:
            return f"Error: {data['error']}"
        
        summary = []
        summary.append(f"Analysis of: {data['file']}")
        summary.append("=" * 80)
        
        # Login history
        logins = data.get('login_history', [])
        if logins:
            summary.append(f"\n📍 Login History: {len(logins)} entries")
            for i, login in enumerate(logins[:5], 1):  # Show first 5
                summary.append(f"   {i}. IP: {login.get('ip', 'N/A')} | "
                             f"Location: {login.get('location', 'N/A')} | "
                             f"Device: {login.get('device', 'N/A')}")
            if len(logins) > 5:
                summary.append(f"   ... and {len(logins) - 5} more")
        
        # Security events
        events = data.get('security_events', [])
        if events:
            summary.append(f"\n🔒 Security Events: {len(events)} found")
            for i, event in enumerate(events[:5], 1):
                summary.append(f"   {i}. {event['keyword'].upper()}")
                summary.append(f"      Context: {event['context'][:100]}...")
            if len(events) > 5:
                summary.append(f"   ... and {len(events) - 5} more")
        
        # IP addresses
        ips = data.get('ip_addresses', [])
        if ips:
            summary.append(f"\n🌐 Unique IP Addresses: {len(ips)}")
            for ip in ips[:10]:  # Show first 10
                summary.append(f"   • {ip}")
            if len(ips) > 10:
                summary.append(f"   ... and {len(ips) - 10} more")
        
        return "\n".join(summary)


def main():
    """Demo usage of the parser."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python parse_facebook_html.py <html_file>")
        print("\nExample:")
        print("  python parse_facebook_html.py evidence/security_and_login_information.html")
        sys.exit(1)
    
    html_file = sys.argv[1]
    
    if not Path(html_file).exists():
        print(f"Error: File not found: {html_file}")
        sys.exit(1)
    
    print("Parsing Facebook HTML file...")
    print("=" * 80)
    
    parser = FacebookHTMLParser(html_file)
    print(parser.generate_summary())
    
    print("\n" + "=" * 80)
    print("✅ Parsing complete")


if __name__ == '__main__':
    main()
