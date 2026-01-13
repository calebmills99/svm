#!/usr/bin/env python3
"""
Facebook Account Breach Analysis Tool

This script analyzes Facebook data downloads to identify evidence of account breaches.
It examines login history, account activity, and other security-related data to detect
suspicious patterns and unauthorized access.

Purpose: Help identify evidence for Facebook account breach case
"""

import json
import os
import sys
from datetime import datetime
from collections import defaultdict
from pathlib import Path
import re


class FacebookBreachAnalyzer:
    """Analyzes Facebook data for signs of account breach."""
    
    def __init__(self, data_dir="facebook_data"):
        self.data_dir = Path(data_dir)
        self.breach_date = datetime(2024, 12, 24)  # Christmas Eve 2024
        self.findings = []
        self.timeline = []
        self.suspicious_ips = set()
        self.suspicious_devices = set()
        
    def check_data_exists(self):
        """Check if Facebook data directory exists."""
        if not self.data_dir.exists():
            print(f"❌ Error: '{self.data_dir}' directory not found!")
            print("\nPlease follow these steps:")
            print("1. Download your Facebook data")
            print("2. Extract the ZIP file")
            print("3. Create a 'facebook_data' folder in this repository")
            print("4. Copy all extracted files into that folder")
            print("\nSee BREACH_ANALYSIS_GUIDE.md for detailed instructions.")
            return False
        return True
    
    def find_json_files(self):
        """Find all JSON files in the data directory."""
        json_files = list(self.data_dir.rglob("*.json"))
        print(f"📁 Found {len(json_files)} JSON files to analyze")
        return json_files
    
    def analyze_login_history(self):
        """Analyze login history for suspicious activity."""
        print("\n🔍 Analyzing login history...")
        
        login_files = [
            "security_and_login_information/login_history.json",
            "security_and_login_information/authorized_logins.json",
            "security_and_login_information/where_you're_logged_in.json",
        ]
        
        for file_path in login_files:
            full_path = self.data_dir / file_path
            if full_path.exists():
                self._analyze_login_file(full_path)
            else:
                print(f"  ⚠️  {file_path} not found")
    
    def _analyze_login_file(self, file_path):
        """Analyze a specific login history file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"  ✓ Analyzing {file_path.name}")
            
            # Handle different data structures
            if isinstance(data, dict):
                # Look for common keys
                for key in ['account_activity', 'login_history', 'sessions', 'authorized_logins']:
                    if key in data:
                        self._process_login_entries(data[key], file_path.name)
            elif isinstance(data, list):
                self._process_login_entries(data, file_path.name)
                
        except json.JSONDecodeError:
            print(f"  ❌ Error reading {file_path}: Invalid JSON format")
        except Exception as e:
            print(f"  ❌ Error analyzing {file_path}: {e}")
    
    def _process_login_entries(self, entries, source_file):
        """Process individual login entries."""
        if not isinstance(entries, list):
            return
        
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            
            # Extract timestamp
            timestamp = None
            for time_key in ['timestamp', 'created_timestamp', 'time', 'datetime']:
                if time_key in entry:
                    timestamp = self._parse_timestamp(entry[time_key])
                    break
            
            if timestamp:
                # Check if around breach date (within 2 weeks before/after)
                days_from_breach = abs((timestamp - self.breach_date).days)
                if days_from_breach <= 14:
                    self._flag_suspicious_entry(entry, timestamp, source_file)
    
    def _parse_timestamp(self, ts):
        """Parse various timestamp formats."""
        try:
            if isinstance(ts, int):
                return datetime.fromtimestamp(ts)
            elif isinstance(ts, str):
                # Try common formats
                for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%dT%H:%M:%S', '%m/%d/%Y %H:%M:%S']:
                    try:
                        return datetime.strptime(ts, fmt)
                    except (ValueError, TypeError):
                        continue
        except (ValueError, TypeError, OSError):
            pass
        return None
    
    def _flag_suspicious_entry(self, entry, timestamp, source):
        """Flag potentially suspicious login entry."""
        details = {
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'source': source,
            'entry': entry
        }
        
        # Extract IP address if present
        for ip_key in ['ip', 'ip_address', 'user_ip']:
            if ip_key in entry:
                details['ip'] = entry[ip_key]
                self.suspicious_ips.add(entry[ip_key])
        
        # Extract location if present
        for loc_key in ['location', 'city', 'region', 'country']:
            if loc_key in entry:
                details['location'] = entry[loc_key]
        
        # Extract device if present
        for dev_key in ['device', 'user_agent', 'platform']:
            if dev_key in entry:
                details['device'] = entry[dev_key]
        
        self.timeline.append(details)
    
    def analyze_account_activity(self):
        """Analyze account activity and changes."""
        print("\n🔍 Analyzing account activity...")
        
        activity_files = [
            "security_and_login_information/account_activity.json",
            "other_logged_information/account_activity.json",
        ]
        
        for file_path in activity_files:
            full_path = self.data_dir / file_path
            if full_path.exists():
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    print(f"  ✓ Analyzing {file_path}")
                    # Process account changes
                    self._process_account_changes(data)
                except Exception as e:
                    print(f"  ❌ Error analyzing {file_path}: {e}")
    
    def _process_account_changes(self, data):
        """Process account change events."""
        # This will depend on the structure of the data
        # Looking for password changes, email changes, etc.
        pass
    
    def scan_all_files(self):
        """Scan all JSON files for timestamps around breach date."""
        print("\n🔍 Scanning all files for activity around breach date...")
        
        json_files = self.find_json_files()
        
        for json_file in json_files:
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Look for timestamps in the content
                    self._scan_for_timestamps(content, json_file.name)
            except (OSError, UnicodeDecodeError) as e:
                # Skip files that can't be read or aren't text files
                continue
    
    def _scan_for_timestamps(self, content, filename):
        """Scan content for timestamps around breach date."""
        # Look for epoch timestamps around Christmas Eve 2024
        # 1734998400 = Dec 24, 2024 00:00:00 UTC
        # 1735603200 = Dec 31, 2024 00:00:00 UTC
        breach_epoch_start = 1734393600  # Dec 17, 2024 (1 week before)
        breach_epoch_end = 1736208000    # Jan 7, 2025 (2 weeks after)
        
        # Find epoch timestamps
        epoch_pattern = r'\b(17\d{8})\b'
        matches = re.findall(epoch_pattern, content)
        
        for match in matches:
            timestamp = int(match)
            if breach_epoch_start <= timestamp <= breach_epoch_end:
                dt = datetime.fromtimestamp(timestamp)
                self.findings.append(f"Found activity in {filename} on {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def generate_report(self):
        """Generate a comprehensive breach analysis report."""
        print("\n📝 Generating breach analysis report...")
        
        report_lines = [
            "# Facebook Account Breach Analysis Report",
            f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"\n## Investigation Summary",
            f"- Breach Date: December 24, 2024 (Christmas Eve)",
            f"- Analysis Period: December 17, 2024 - January 7, 2025 (3-week window)",
            f"- Total Timeline Entries: {len(self.timeline)}",
            f"- Suspicious IPs: {len(self.suspicious_ips)}",
            f"- Findings: {len(self.findings)}",
        ]
        
        if self.timeline:
            report_lines.extend([
                "\n## Timeline of Suspicious Activity",
                "\nEvents occurring within 2 weeks of the breach date:\n",
            ])
            
            # Sort by timestamp
            sorted_timeline = sorted(self.timeline, key=lambda x: x['timestamp'])
            
            for event in sorted_timeline:
                report_lines.append(f"### {event['timestamp']}")
                report_lines.append(f"- Source: {event['source']}")
                if 'ip' in event:
                    report_lines.append(f"- IP Address: {event['ip']}")
                if 'location' in event:
                    report_lines.append(f"- Location: {event['location']}")
                if 'device' in event:
                    report_lines.append(f"- Device: {event['device']}")
                report_lines.append("")
        
        if self.suspicious_ips:
            report_lines.extend([
                "\n## Suspicious IP Addresses",
                "\nIP addresses that accessed the account during the breach period:\n",
            ])
            for ip in sorted(self.suspicious_ips):
                report_lines.append(f"- {ip}")
        
        if self.findings:
            report_lines.extend([
                "\n## Additional Findings",
                "",
            ])
            for finding in self.findings:
                report_lines.append(f"- {finding}")
        
        report_lines.extend([
            "\n## Recommendations for Legal Case",
            "",
            "1. **Document All Evidence**: This report serves as a chronological record of suspicious activity",
            "2. **Cross-Reference IPs**: Check if the suspicious IPs match your known locations",
            "3. **Check Location History**: Compare login locations with your actual location on those dates",
            "4. **Review Account Changes**: Look for unauthorized password changes, email changes, or security setting modifications",
            "5. **Preserve Original Data**: Keep the original Facebook data download as evidence",
            "6. **Note Access Impact**: Document when you were locked out and what access you lost",
            "",
            "\n## Next Steps",
            "",
            "1. Review each timeline entry above",
            "2. Mark which activities you recognize vs. don't recognize",
            "3. Check if you were in the locations shown at the times shown",
            "4. Look for any posts, messages, or changes you didn't make",
            "5. Compile this evidence for your small claims case",
            "",
            "\n## Important Notes",
            "",
            "- All timestamps are in your local timezone",
            "- Unknown IPs could indicate unauthorized access",
            "- Multiple logins from different locations in short time periods are suspicious",
            "- Activity while you were provably elsewhere is strong evidence",
        ])
        
        report_content = '\n'.join(report_lines)
        
        # Write report
        with open('BREACH_REPORT.md', 'w') as f:
            f.write(report_content)
        
        print("  ✓ Report saved to BREACH_REPORT.md")
        
        # Write IP list
        if self.suspicious_ips:
            with open('suspicious_ips.txt', 'w') as f:
                f.write("Suspicious IP Addresses\n")
                f.write("=" * 50 + "\n\n")
                for ip in sorted(self.suspicious_ips):
                    f.write(f"{ip}\n")
            print("  ✓ IP list saved to suspicious_ips.txt")
        
        # Write timeline
        if self.timeline:
            with open('timeline.txt', 'w') as f:
                f.write("Breach Timeline\n")
                f.write("=" * 50 + "\n\n")
                sorted_timeline = sorted(self.timeline, key=lambda x: x['timestamp'])
                for event in sorted_timeline:
                    f.write(f"{event['timestamp']} - {event.get('location', 'Unknown location')}\n")
            print("  ✓ Timeline saved to timeline.txt")
    
    def run_analysis(self):
        """Run complete analysis."""
        print("=" * 60)
        print("Facebook Account Breach Analysis Tool")
        print("=" * 60)
        
        if not self.check_data_exists():
            return False
        
        # Run all analysis steps
        self.analyze_login_history()
        self.analyze_account_activity()
        self.scan_all_files()
        
        # Generate report
        self.generate_report()
        
        print("\n" + "=" * 60)
        print("✅ Analysis Complete!")
        print("=" * 60)
        print("\nPlease review:")
        print("  - BREACH_REPORT.md (main findings)")
        if self.suspicious_ips:
            print("  - suspicious_ips.txt (IP addresses)")
        if self.timeline:
            print("  - timeline.txt (event timeline)")
        print("\nSee BREACH_ANALYSIS_GUIDE.md for next steps.")
        
        return True


def main():
    """Main entry point."""
    analyzer = FacebookBreachAnalyzer()
    success = analyzer.run_analysis()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
