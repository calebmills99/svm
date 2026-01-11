#!/usr/bin/env python3
"""
Quick Check Script - Verifies Facebook data structure

This script helps you verify that your Facebook data download is in the correct
format and location before running the full analysis.
"""

import os
from pathlib import Path
import json


def check_facebook_data():
    """Check if Facebook data directory exists and show structure."""
    
    print("=" * 60)
    print("Facebook Data Structure Checker")
    print("=" * 60)
    
    data_dir = Path("facebook_data")
    
    if not data_dir.exists():
        print("\n❌ 'facebook_data' directory not found!")
        print("\nTo fix this:")
        print("1. Create a folder named 'facebook_data' in this directory")
        print("2. Extract your Facebook data ZIP file")
        print("3. Copy all extracted files into the 'facebook_data' folder")
        print("\nExpected structure:")
        print("  repository/")
        print("  ├── facebook_data/")
        print("  │   ├── security_and_login_information/")
        print("  │   ├── messages/")
        print("  │   ├── posts/")
        print("  │   └── ... (other Facebook data folders)")
        print("  ├── analyze_breach.py")
        print("  └── README.md")
        return False
    
    print("\n✅ 'facebook_data' directory found!\n")
    
    # Check for key security files
    important_files = [
        "security_and_login_information/login_history.json",
        "security_and_login_information/authorized_logins.json",
        "security_and_login_information/where_you're_logged_in.json",
        "security_and_login_information/account_activity.json",
    ]
    
    print("Checking for important security files:\n")
    found_files = []
    missing_files = []
    
    for file_path in important_files:
        full_path = data_dir / file_path
        if full_path.exists():
            # Check if it's valid JSON
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    size = full_path.stat().st_size
                    print(f"  ✅ {file_path} ({size:,} bytes)")
                    found_files.append(file_path)
            except json.JSONDecodeError:
                print(f"  ⚠️  {file_path} exists but is not valid JSON")
            except Exception as e:
                print(f"  ⚠️  {file_path} exists but cannot be read: {e}")
        else:
            print(f"  ❌ {file_path} not found")
            missing_files.append(file_path)
    
    # List all JSON files found
    all_json = list(data_dir.rglob("*.json"))
    print(f"\n📊 Total JSON files found: {len(all_json)}")
    
    if len(all_json) > 0:
        print("\nSample of files in your data:")
        for json_file in sorted(all_json)[:10]:
            rel_path = json_file.relative_to(data_dir)
            size = json_file.stat().st_size
            print(f"  - {rel_path} ({size:,} bytes)")
        if len(all_json) > 10:
            print(f"  ... and {len(all_json) - 10} more files")
    
    print("\n" + "=" * 60)
    
    if found_files:
        print("✅ Ready to run analysis!")
        print("\nNext step:")
        print("  python3 analyze_breach.py")
    else:
        print("⚠️  No security files found")
        print("\nThis could mean:")
        print("1. Your Facebook data is in a different format")
        print("2. The files are in a different location")
        print("3. You need to request a new download with security data")
        print("\nThe analysis will still scan all JSON files for relevant data.")
    
    print("=" * 60)
    
    return True


if __name__ == "__main__":
    check_facebook_data()
