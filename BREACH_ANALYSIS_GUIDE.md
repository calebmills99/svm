# Facebook Account Breach Analysis Guide

## Overview
This guide will help you analyze your Facebook data download to identify evidence of account breach that occurred around Christmas Eve 2024.

## Step 1: Upload Your Facebook Data

### How to Get Your Facebook Data
If you haven't already downloaded your Facebook data:
1. Go to Facebook Settings > Privacy > Download Your Information
2. Select "All time" for the date range
3. Select "High" quality
4. Select all data categories (especially Security and Login Information)
5. Request the download

### Expected Files
Facebook typically provides data in JSON format within a ZIP file. Common important files include:
- `security_and_login_information/login_history.json` - All login attempts
- `security_and_login_information/account_activity.json` - Account changes
- `security_and_login_information/authorized_logins.json` - Devices that logged in
- `security_and_login_information/where_you're_logged_in.json` - Active sessions
- `apps_and_websites/` - Connected apps
- `messages/` - Message history
- `your_posts/` - Posts made

### Upload Instructions
1. Extract the ZIP file from Facebook
2. Create a folder called `facebook_data` in this repository
3. Copy all files maintaining the folder structure
4. **IMPORTANT**: Review and redact any personal information you don't want to share before committing
5. Add the files to git and commit

## Step 2: Run Analysis Scripts

Once you've uploaded the data, run:
```bash
python3 analyze_breach.py
```

This will generate a report identifying:
- Suspicious login locations
- Unusual login times
- New devices/IPs
- Account changes during the breach period
- Timeline of events

## Step 3: Review the Report

The script will create:
- `BREACH_REPORT.md` - Detailed findings
- `timeline.txt` - Chronological event timeline
- `suspicious_ips.txt` - List of suspicious IP addresses

## Key Indicators of Compromise

Look for:
- ✓ Logins from unfamiliar locations
- ✓ Logins from unfamiliar devices
- ✓ Multiple failed login attempts
- ✓ Password changes you didn't make
- ✓ Email changes
- ✓ New authorized apps
- ✓ Posts/messages you didn't create
- ✓ Unusual activity times (e.g., when you were asleep)

## Important Notes for Legal Proceedings

For your small claims case:
1. **Preserve Evidence**: Don't delete any files
2. **Document Everything**: The scripts will help create a chronological record
3. **Note Damages**: Document any harm caused (locked out of account, loss of data, etc.)
4. **Timeline**: The breach timeline is critical evidence

## Privacy Considerations

Before committing data to GitHub:
- Remove or redact personal messages
- Consider redacting phone numbers and email addresses
- You may want to keep this repository private
- Replace real names with pseudonyms if needed

## Need Help?

If you encounter issues:
1. Check that your Facebook data is in the correct format
2. Ensure Python 3 is installed
3. Review error messages from the analysis scripts
4. Create an issue in this repository with details
