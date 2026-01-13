#!/usr/bin/env python3
"""
Facebook Account Breach Evidence Analyzer

This script analyzes files downloaded from Meta/Facebook to identify
potential evidence of unauthorized account access or security breaches.

Usage:
    python analyze_evidence.py [--evidence-dir DIRECTORY] [--output OUTPUT_FILE]

Author: Analysis Tool for Caleb Stewart
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any


class EvidenceAnalyzer:
    """Main class for analyzing Facebook evidence files."""
    
    def __init__(self, evidence_dir: str = "evidence"):
        """Initialize the analyzer with the evidence directory."""
        self.evidence_dir = Path(evidence_dir)
        self.findings = []
        self.timeline = []
        self.suspicious_activities = []
        
    def scan_directory(self) -> Dict[str, List[Path]]:
        """Scan the evidence directory and categorize files."""
        if not self.evidence_dir.exists():
            print(f"⚠️  Evidence directory not found: {self.evidence_dir}")
            print(f"   Please create the directory and add your files.")
            return {}
        
        files = {
            'pdf': [],
            'html': [],
            'json': []
        }
        
        for file_path in self.evidence_dir.rglob('*'):
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext == '.pdf':
                    files['pdf'].append(file_path)
                elif ext in ['.html', '.htm']:
                    files['html'].append(file_path)
                elif ext == '.json':
                    files['json'].append(file_path)
                # Skip other file types - they're not analyzed
        
        return files
    
    def analyze_json_files(self, json_files: List[Path]):
        """Analyze JSON files for security-relevant information."""
        print("\n📊 Analyzing JSON files...")
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                print(f"   ✓ Parsed: {json_file.name}")
                
                # Look for security-related fields
                self._analyze_json_data(data, json_file.name)
                
            except json.JSONDecodeError as e:
                print(f"   ✗ Error parsing {json_file.name}: {e}")
            except Exception as e:
                print(f"   ✗ Error reading {json_file.name}: {e}")
    
    def _analyze_json_data(self, data: Any, source: str):
        """Recursively analyze JSON data for security indicators."""
        if isinstance(data, dict):
            # Check for security-related keys
            security_keys = [
                'login', 'session', 'ip', 'device', 'location',
                'access', 'unauthorized', 'breach', 'security',
                'password', 'authentication', 'token'
            ]
            
            for key, value in data.items():
                key_lower = str(key).lower()
                if any(sec_key in key_lower for sec_key in security_keys):
                    self.findings.append({
                        'source': source,
                        'type': 'security_data',
                        'field': key,
                        'value': value
                    })
                
                # Recurse into nested structures
                self._analyze_json_data(value, source)
        
        elif isinstance(data, list):
            for item in data:
                self._analyze_json_data(item, source)
    
    def analyze_html_files(self, html_files: List[Path]):
        """Analyze HTML files for security information."""
        print("\n🌐 Analyzing HTML files...")
        
        for html_file in html_files:
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"   ✓ Read: {html_file.name}")
                
                # Basic analysis - look for security-related keywords
                suspicious_keywords = [
                    'unauthorized', 'breach', 'hacked', 'compromised',
                    'suspicious activity', 'unrecognized', 'unknown device',
                    'failed login', 'password changed', 'security alert'
                ]
                
                for keyword in suspicious_keywords:
                    if keyword.lower() in content.lower():
                        self.suspicious_activities.append({
                            'source': html_file.name,
                            'keyword': keyword,
                            'type': 'keyword_match'
                        })
                
            except Exception as e:
                print(f"   ✗ Error reading {html_file.name}: {e}")
    
    def analyze_pdf_files(self, pdf_files: List[Path]):
        """Analyze PDF files for security-relevant information."""
        print("\n📄 Analyzing PDF files...")
        
        # Try to import PDF libraries
        pdf_reader = None
        try:
            import pdfplumber
            pdf_reader = 'pdfplumber'
        except ImportError:
            try:
                import PyPDF2
                pdf_reader = 'PyPDF2'
            except ImportError:
                print("   ⚠️  PDF libraries not available. Install with:")
                print("      pip install PyPDF2 pdfplumber")
                for pdf_file in pdf_files:
                    print(f"   • Skipped: {pdf_file.name}")
                return
        
        for pdf_file in pdf_files:
            try:
                text = ""
                
                if pdf_reader == 'pdfplumber':
                    import pdfplumber
                    with pdfplumber.open(pdf_file) as pdf:
                        for page in pdf.pages:
                            page_text = page.extract_text()
                            if page_text:
                                text += page_text + "\n"
                else:
                    import PyPDF2
                    with open(pdf_file, 'rb') as f:
                        reader = PyPDF2.PdfReader(f)
                        for page in reader.pages:
                            page_text = page.extract_text()
                            if page_text:
                                text += page_text + "\n"
                
                if text:
                    print(f"   ✓ Extracted text from: {pdf_file.name}")
                    
                    # Analyze extracted text for security indicators
                    self._analyze_pdf_text(text, pdf_file.name)
                else:
                    print(f"   ⚠️  No text extracted from: {pdf_file.name}")
                    
            except Exception as e:
                print(f"   ✗ Error reading {pdf_file.name}: {e}")
    
    def _analyze_pdf_text(self, text: str, source: str):
        """Analyze extracted PDF text for security indicators."""
        # Look for security-related keywords
        suspicious_keywords = [
            'unauthorized', 'breach', 'hacked', 'compromised',
            'suspicious activity', 'unrecognized', 'unknown device',
            'failed login', 'password changed', 'security alert',
            'account recovery', 'two-factor', 'verification'
        ]
        
        text_lower = text.lower()
        
        for keyword in suspicious_keywords:
            if keyword in text_lower:
                # Find context around the keyword
                idx = text_lower.find(keyword)
                start = max(0, idx - 50)
                end = min(len(text), idx + len(keyword) + 100)
                context = text[start:end].replace('\n', ' ').strip()
                
                self.suspicious_activities.append({
                    'source': source,
                    'keyword': keyword,
                    'context': context,
                    'type': 'pdf_keyword_match'
                })
        
        # Extract IP addresses
        import re
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        ips = re.findall(ip_pattern, text)
        
        for ip in set(ips):
            # Basic validation: each octet should be 0-255
            octets = ip.split('.')
            if all(0 <= int(o) <= 255 for o in octets):
                self.findings.append({
                    'source': source,
                    'type': 'ip_address',
                    'value': ip
                })
    
    def generate_report(self) -> str:
        """Generate a human-readable analysis report."""
        report = []
        report.append("=" * 80)
        report.append("FACEBOOK ACCOUNT BREACH EVIDENCE ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Analyzed by: Evidence Analyzer for Caleb Stewart\n")
        
        # Summary
        report.append("\n" + "=" * 80)
        report.append("SUMMARY")
        report.append("=" * 80)
        report.append(f"Total findings: {len(self.findings)}")
        report.append(f"Suspicious activities detected: {len(self.suspicious_activities)}")
        
        # Suspicious Activities
        if self.suspicious_activities:
            report.append("\n" + "=" * 80)
            report.append("⚠️  SUSPICIOUS ACTIVITIES")
            report.append("=" * 80)
            
            for i, activity in enumerate(self.suspicious_activities, 1):
                report.append(f"\n{i}. {activity['keyword'].upper()}")
                report.append(f"   Source: {activity['source']}")
                report.append(f"   Type: {activity['type']}")
        
        # Detailed Findings
        if self.findings:
            report.append("\n" + "=" * 80)
            report.append("DETAILED FINDINGS")
            report.append("=" * 80)
            
            for i, finding in enumerate(self.findings[:50], 1):  # Limit to first 50
                report.append(f"\n{i}. {finding.get('type', 'Unknown')}")
                report.append(f"   Source: {finding['source']}")
                if 'field' in finding:
                    report.append(f"   Field: {finding['field']}")
                if 'value' in finding:
                    # Truncate long values
                    value_str = str(finding['value'])
                    if len(value_str) > 200:
                        value_str = value_str[:200] + "..."
                    report.append(f"   Value: {value_str}")
            
            if len(self.findings) > 50:
                report.append(f"\n... and {len(self.findings) - 50} more findings")
        
        # Recommendations
        report.append("\n" + "=" * 80)
        report.append("RECOMMENDATIONS")
        report.append("=" * 80)
        report.append("\n1. Review all suspicious activities listed above")
        report.append("2. Change your password immediately if you haven't already")
        report.append("3. Enable two-factor authentication on all accounts")
        report.append("4. Review and revoke access to any suspicious apps")
        report.append("5. Check for any unrecognized devices in your account settings")
        report.append("6. Consider contacting Meta/Facebook support")
        report.append("7. If needed, consult with a cybersecurity professional")
        report.append("8. Document all findings for potential legal action")
        
        report.append("\n" + "=" * 80)
        report.append("END OF REPORT")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def run_analysis(self):
        """Run the complete analysis."""
        print("=" * 80)
        print("FACEBOOK ACCOUNT BREACH EVIDENCE ANALYZER")
        print("=" * 80)
        print(f"\nAnalyzing directory: {self.evidence_dir}\n")
        
        # Scan for files
        files = self.scan_directory()
        
        if not any(files.values()):
            print("\n⚠️  NO FILES FOUND")
            print("\nPlease add your Facebook data files to the 'evidence' directory.")
            print("See ANALYSIS_README.md for instructions.\n")
            return None
        
        # Print file summary
        print("\n📁 Files Found:")
        for file_type, file_list in files.items():
            if file_list:
                print(f"   {file_type.upper()}: {len(file_list)} files")
        
        # Analyze different file types
        if files['json']:
            self.analyze_json_files(files['json'])
        
        if files['html']:
            self.analyze_html_files(files['html'])
        
        if files['pdf']:
            self.analyze_pdf_files(files['pdf'])
        
        # Generate report
        print("\n📝 Generating report...")
        report = self.generate_report()
        
        return report


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Analyze Facebook account breach evidence'
    )
    parser.add_argument(
        '--evidence-dir',
        default='evidence',
        help='Directory containing evidence files (default: evidence)'
    )
    parser.add_argument(
        '--output',
        default='analysis_report.txt',
        help='Output file for the analysis report (default: analysis_report.txt)'
    )
    
    args = parser.parse_args()
    
    # Run analysis
    analyzer = EvidenceAnalyzer(args.evidence_dir)
    report = analyzer.run_analysis()
    
    if report:
        # Save report
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # Also print to console
        print("\n" + report)
        print(f"\n✅ Report saved to: {args.output}")
    else:
        print("\n❌ No analysis performed - no files found")
        print("   Please upload your Facebook data files and try again.\n")


if __name__ == '__main__':
    main()
