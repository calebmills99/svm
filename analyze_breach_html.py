#!/usr/bin/env python3
"""
Facebook Account Breach Analysis Tool - HTML Parser

This script analyzes Facebook data downloads that are in HTML format.
It examines login history, account activity, and security-related data 
to detect suspicious patterns and unauthorized access.

Purpose: Help identify evidence for Facebook account breach case
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from html.parser import HTMLParser


class SecurityDataParser(HTMLParser):
    """Parse security-related data from Facebook HTML files."""
    
    def __init__(self):
        super().__init__()
        self.events = []
        self.current_event = {}
        self.current_label = None
        self.in_table = False
        self.in_section = False
        self.section_title = None
        self.capture_data = False
        self.data_buffer = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'section':
            self.in_section = True
            self.current_event = {}
        elif tag == 'table':
            self.in_table = True
        elif tag == 'td' or tag == 'h2':
            self.capture_data = True
            self.data_buffer = []
    
    def handle_endtag(self, tag):
        if tag == 'section':
            if self.current_event:
                self.events.append(self.current_event.copy())
            self.current_event = {}
            self.in_section = False
        elif tag == 'table':
            self.in_table = False
        elif tag == 'td':
            self.capture_data = False
            data = ''.join(self.data_buffer).strip()
            if self.current_label:
                self.current_event[self.current_label] = data
                self.current_label = None
            else:
                # This might be a label
                self.current_label = data.lower().replace(' ', '_').rstrip(':')
        elif tag == 'h2':
            self.capture_data = False
            title = ''.join(self.data_buffer).strip()
            if title:
                self.current_event['event_type'] = title
                self.section_title = title
    
    def handle_data(self, data):
        if self.capture_data:
            self.data_buffer.append(data)


class FacebookBreachAnalyzerHTML:
    """Analyzes Facebook HTML data for signs of account breach."""
    
    def __init__(self, data_dir=None):
        self.data_dir = None
        self.findings = []
        self.timeline = []
        self.all_events = []
        self.suspicious_ips = set()
        self.account_info = {}
        self.breach_date = datetime(2024, 12, 24)  # Christmas Eve 2024
        
        # Try to auto-detect data directory
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            # Look for facebook-* directories
            for item in Path('.').iterdir():
                if item.is_dir() and item.name.startswith('facebook-'):
                    self.data_dir = item
                    break
    
    def check_data_exists(self):
        """Check if Facebook data directory exists."""
        if not self.data_dir or not self.data_dir.exists():
            print("❌ Error: No Facebook data directory found!")
            print("\nLooking for a directory starting with 'facebook-'...")
            return False
        print(f"✓ Found Facebook data directory: {self.data_dir}")
        return True
    
    def parse_html_file(self, file_path):
        """Parse a Facebook HTML file and extract data."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            parser = SecurityDataParser()
            parser.feed(content)
            return parser.events
        except Exception as e:
            print(f"  ⚠️ Error parsing {file_path}: {e}")
            return []
    
    def parse_html_simple(self, file_path):
        """Simple regex-based parsing of HTML files."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            events = []
            
            # Extract sections with table data
            section_pattern = r'<section[^>]*>.*?</section>'
            sections = re.findall(section_pattern, content, re.DOTALL)
            
            for section in sections:
                event = {}
                
                # Get section title (h2)
                h2_match = re.search(r'<h2[^>]*>([^<]+)</h2>', section)
                if h2_match:
                    event['event_type'] = h2_match.group(1).strip()
                
                # Get table data - look for td pairs (label/value)
                td_pattern = r'<td[^>]*>([^<]*)</td>'
                tds = re.findall(td_pattern, section)
                
                i = 0
                while i < len(tds) - 1:
                    label = tds[i].strip().lower().replace(' ', '_')
                    value = tds[i + 1].strip()
                    if label and value:
                        event[label] = value
                    i += 2
                
                if event:
                    events.append(event)
            
            return events
        except Exception as e:
            print(f"  ⚠️ Error parsing {file_path}: {e}")
            return []
    
    def analyze_security_files(self):
        """Analyze security and login information files."""
        print("\n🔍 Analyzing security and login information...")
        
        security_dir = self.data_dir / "security_and_login_information"
        if not security_dir.exists():
            print(f"  ⚠️ Security directory not found: {security_dir}")
            return
        
        # Key security files
        security_files = [
            "account_activity.html",
            "account_status_changes.html",
            "ip_address_activity.html",
            "logins_and_logouts.html",
            "login_protection_data.html",
            "your_facebook_activity_history.html",
            "registration_information.html",
            "record_details.html"
        ]
        
        for filename in security_files:
            file_path = security_dir / filename
            if file_path.exists():
                print(f"  ✓ Analyzing {filename}")
                events = self.parse_html_simple(file_path)
                for event in events:
                    event['source_file'] = filename
                    self.all_events.append(event)
    
    def analyze_profile_info(self):
        """Analyze profile information."""
        print("\n🔍 Analyzing profile information...")
        
        profile_file = self.data_dir / "personal_information" / "profile_information" / "profile_information.html"
        if profile_file.exists():
            try:
                with open(profile_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract profile data
                name_match = re.search(r'<th>Name</th><td>([^<]+)', content)
                if name_match:
                    self.account_info['name'] = name_match.group(1).strip()
                
                reg_match = re.search(r'<th>Registration date</th><td>([^<]+)', content)
                if reg_match:
                    self.account_info['registration_date'] = reg_match.group(1).strip()
                
                email_match = re.search(r'<th>Emails</th><td><ul><li>([^<]+)', content)
                if email_match:
                    self.account_info['email'] = email_match.group(1).strip().replace('&#064;', '@')
                
                profile_match = re.search(r'<th>Profile</th><td><a[^>]+>([^<]+)', content)
                if profile_match:
                    self.account_info['profile_url'] = profile_match.group(1).strip()
                
                print(f"  ✓ Found account: {self.account_info.get('name', 'Unknown')}")
                print(f"  ✓ Registered: {self.account_info.get('registration_date', 'Unknown')}")
                
            except Exception as e:
                print(f"  ⚠️ Error reading profile info: {e}")
    
    def extract_timestamps_and_ips(self):
        """Extract timestamps and IP addresses from events."""
        print("\n🔍 Extracting timestamps and IP addresses...")
        
        for event in self.all_events:
            # Get timestamp
            timestamp_str = event.get('time', '')
            if not timestamp_str:
                # Check for date patterns in event type or other fields
                for key, value in event.items():
                    if isinstance(value, str) and re.search(r'\d{4}', value):
                        timestamp_str = value
                        break
            
            if timestamp_str:
                event['timestamp_raw'] = timestamp_str
            
            # Get IP address
            ip = event.get('ip_address', '')
            if ip:
                self.suspicious_ips.add(ip)
            
            # Get location
            location_parts = []
            for key in ['city', 'region', 'country']:
                if key in event:
                    location_parts.append(event[key])
            if location_parts:
                event['location'] = ', '.join(location_parts)
        
        print(f"  ✓ Found {len(self.suspicious_ips)} unique IP addresses")
    
    def generate_report(self):
        """Generate a comprehensive breach analysis report."""
        print("\n📝 Generating breach analysis report...")
        
        report = []
        report.append("# Facebook Account Breach Analysis Report")
        report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Data Directory:** {self.data_dir}")
        
        # Account Information
        report.append("\n## Account Information")
        report.append("")
        if self.account_info:
            report.append(f"- **Name:** {self.account_info.get('name', 'N/A')}")
            report.append(f"- **Email:** {self.account_info.get('email', 'N/A')}")
            report.append(f"- **Registration Date:** {self.account_info.get('registration_date', 'N/A')}")
            report.append(f"- **Profile URL:** {self.account_info.get('profile_url', 'N/A')}")
        
        # Critical Finding
        reg_date = self.account_info.get('registration_date', '')
        if '2025' in reg_date:
            report.append("\n## ⚠️ CRITICAL FINDING")
            report.append("")
            report.append("**This is a NEW Facebook account created in 2025, NOT the original breached account.**")
            report.append("")
            report.append("Key observations:")
            report.append(f"- Account registration date: {reg_date}")
            report.append("- The original breach occurred on Christmas Eve 2024")
            report.append("- This data download is from a new/recovered account")
            report.append("")
            report.append("**Implications for legal case:**")
            report.append("- This data shows Meta created a new account for you after the breach")
            report.append("- The original account data (with breach evidence) may need to be requested separately")
            report.append("- This account's activity is from AFTER the breach period")
        
        # Analysis Summary
        report.append("\n## Analysis Summary")
        report.append("")
        report.append(f"- **Total Events Found:** {len(self.all_events)}")
        report.append(f"- **Unique IP Addresses:** {len(self.suspicious_ips)}")
        
        # Event Types
        event_types = {}
        for event in self.all_events:
            etype = event.get('event_type', 'Unknown')
            event_types[etype] = event_types.get(etype, 0) + 1
        
        if event_types:
            report.append("\n## Event Types")
            report.append("")
            for etype, count in sorted(event_types.items(), key=lambda x: -x[1]):
                report.append(f"- {etype}: {count}")
        
        # Timeline of Events
        report.append("\n## Timeline of Events")
        report.append("")
        
        for event in self.all_events:
            etype = event.get('event_type', 'Unknown Event')
            time = event.get('time', event.get('timestamp_raw', 'Unknown time'))
            ip = event.get('ip_address', '')
            location = event.get('location', '')
            source = event.get('source_file', '')
            
            report.append(f"### {etype}")
            report.append(f"- **Time:** {time}")
            if ip:
                report.append(f"- **IP Address:** {ip}")
            if location:
                report.append(f"- **Location:** {location}")
            report.append(f"- **Source:** {source}")
            report.append("")
        
        # IP Addresses
        if self.suspicious_ips:
            report.append("\n## IP Addresses")
            report.append("")
            report.append("IP addresses found in account activity:")
            report.append("")
            for ip in sorted(self.suspicious_ips):
                report.append(f"- `{ip}`")
        
        # Recommendations
        report.append("\n## Recommendations for Legal Case")
        report.append("")
        report.append("### Immediate Actions")
        report.append("")
        report.append("1. **Request Original Account Data**: Contact Meta to request the complete data")
        report.append("   download from your ORIGINAL account (breached on Christmas Eve 2024)")
        report.append("")
        report.append("2. **Document Timeline**: Create a detailed timeline showing:")
        report.append("   - When you last had legitimate access to your account")
        report.append("   - When you first noticed something was wrong")
        report.append("   - When the account was disabled")
        report.append("   - All attempts to contact Meta for recovery")
        report.append("")
        report.append("3. **Evidence Collection**: Gather all supporting evidence:")
        report.append("   - Screenshots of any error messages")
        report.append("   - Emails from Meta/Facebook")
        report.append("   - Records of support requests")
        report.append("   - Any notifications about suspicious activity")
        report.append("")
        report.append("### For Small Claims Court")
        report.append("")
        report.append("1. **Demonstrate Damages**: Document any financial losses, lost access to")
        report.append("   photos/memories, business impacts, or emotional distress")
        report.append("")
        report.append("2. **Show Meta's Failure**: Demonstrate that Meta:")
        report.append("   - Failed to protect your account adequately")
        report.append("   - Did not respond appropriately to the breach")
        report.append("   - Did not provide adequate support for account recovery")
        report.append("")
        report.append("3. **Request Specific Relief**: Be clear about what you're asking for:")
        report.append("   - Access to original account data")
        report.append("   - Compensation for documented losses")
        report.append("   - Clear explanation of what happened")
        
        report.append("\n## Data Quality Notes")
        report.append("")
        report.append("- This analysis was performed on HTML-formatted Facebook data")
        report.append("- The data appears to be from a newly created account (July 2025)")
        report.append("- For breach evidence from December 2024, additional data may be needed")
        
        report_content = '\n'.join(report)
        
        # Write report
        with open('BREACH_REPORT.md', 'w') as f:
            f.write(report_content)
        print("  ✓ Report saved to BREACH_REPORT.md")
        
        # Write IP list
        if self.suspicious_ips:
            with open('suspicious_ips.txt', 'w') as f:
                f.write("IP Addresses Found in Account Activity\n")
                f.write("=" * 50 + "\n\n")
                for ip in sorted(self.suspicious_ips):
                    f.write(f"{ip}\n")
            print("  ✓ IP list saved to suspicious_ips.txt")
        
        # Write timeline
        with open('timeline.txt', 'w') as f:
            f.write("Account Activity Timeline\n")
            f.write("=" * 50 + "\n\n")
            for event in self.all_events:
                etype = event.get('event_type', 'Unknown')
                time = event.get('time', 'Unknown time')
                f.write(f"{time} - {etype}\n")
        print("  ✓ Timeline saved to timeline.txt")
        
        return report_content
    
    def run_analysis(self):
        """Run complete analysis."""
        print("=" * 60)
        print("Facebook Account Breach Analysis Tool (HTML Parser)")
        print("=" * 60)
        
        if not self.check_data_exists():
            return False
        
        # Run analysis
        self.analyze_profile_info()
        self.analyze_security_files()
        self.extract_timestamps_and_ips()
        
        # Generate report
        self.generate_report()
        
        print("\n" + "=" * 60)
        print("✅ Analysis Complete!")
        print("=" * 60)
        print("\nPlease review:")
        print("  - BREACH_REPORT.md (main findings)")
        print("  - suspicious_ips.txt (IP addresses)")
        print("  - timeline.txt (event timeline)")
        
        return True


def main():
    """Main entry point."""
    data_dir = sys.argv[1] if len(sys.argv) > 1 else None
    analyzer = FacebookBreachAnalyzerHTML(data_dir)
    success = analyzer.run_analysis()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
