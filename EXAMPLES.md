# Example Usage Guide

## Testing the Analysis Tools

Since no actual Facebook data files are currently available, here's how to test the tools with sample data:

### Create Sample Data Structure

```bash
# Create directory structure
mkdir -p evidence/html evidence/data evidence/pdfs

# The analysis tools will work once you add real files here
```

### Testing with Your Own Data

1. **Download your Facebook data:**
   - Go to Facebook Settings
   - Click "Your Facebook Information"
   - Click "Download Your Information"
   - Select date range and format (HTML or JSON recommended)
   - Request download
   - Wait for email notification (can take hours or days)
   - Download the file

2. **Extract the archive:**
   ```bash
   unzip facebook-*.zip -d evidence/
   ```

3. **Run the analyzer:**
   ```bash
   python analyze_evidence.py --evidence-dir evidence
   ```

### What to Look For in Your Data

#### Critical Files from Facebook Data Export:

1. **security_and_login_information/**
   - Contains login history
   - IP addresses used
   - Devices that accessed your account
   - **This is the most important folder for breach evidence**

2. **account_activity/**
   - Password changes
   - Email/phone changes
   - Security settings changes

3. **apps_and_websites/**
   - Third-party apps with access
   - Websites connected to your Facebook

4. **your_posts/**
   - Posts you made (or that were made from your account)

5. **messages/**
   - Direct messages
   - Could show unauthorized communication

### Analyzing Specific Files

#### For HTML files:
```bash
python parse_facebook_html.py evidence/security_and_login_information.html
```

#### For all files:
```bash
python analyze_evidence.py --evidence-dir evidence --output detailed_report.txt
```

### What the Tools Will Find

The analysis tools search for:

1. **Suspicious Login Patterns:**
   - Logins from unfamiliar locations
   - Unusual IP addresses
   - New devices
   - Login times that don't match your schedule

2. **Security Events:**
   - Password changes
   - Recovery email changes
   - 2FA modifications
   - Security questions changed

3. **Unauthorized Activity:**
   - Posts you didn't make
   - Messages you didn't send
   - Friend requests you didn't send
   - Apps you didn't authorize

4. **Timeline Anomalies:**
   - Gaps in activity (account locked?)
   - Bursts of unusual activity
   - Multiple simultaneous sessions

### Example Output

When you run the analysis, you'll get:

```
================================================================================
FACEBOOK ACCOUNT BREACH EVIDENCE ANALYZER
================================================================================

Analyzing directory: evidence

📁 Files Found:
   HTML: 15 files
   JSON: 23 files
   PDF: 2 files

📊 Analyzing JSON files...
   ✓ Parsed: security_and_login_information.json
   ✓ Parsed: account_activity.json
   ...

🌐 Analyzing HTML files...
   ✓ Read: security_and_login_information.html
   ⚠️  SUSPICIOUS KEYWORD FOUND: "unrecognized device"
   ...

📝 Generating report...

✅ Report saved to: analysis_report.txt
```

### Understanding the Report

The report will include:

1. **Summary Section:**
   - Total number of findings
   - Count of suspicious activities
   - Quick overview

2. **Suspicious Activities:**
   - Detailed list of potential security concerns
   - Contextualized information
   - Source files

3. **Detailed Findings:**
   - Complete data extracted
   - Organized by category
   - Cross-referenced

4. **Recommendations:**
   - Immediate actions to take
   - Security best practices
   - Next steps

### Common Indicators of Breach

Look for these in your report:

| Indicator | What It Means | Severity |
|-----------|---------------|----------|
| Unknown IP addresses | Someone accessed from a different location | 🔴 High |
| Unrecognized devices | New device used to login | 🔴 High |
| Password changed (not by you) | Account compromised | 🔴 Critical |
| Messages sent at odd times | Automated or unauthorized activity | 🟡 Medium |
| New apps authorized | Malicious app access | 🟡 Medium |
| Unusual friend requests | Account being used for spam | 🟢 Low |

### After Running Analysis

1. **Save all results** - Keep copies of:
   - Original Facebook data files
   - Analysis reports
   - Any screenshots

2. **Take immediate action:**
   - Change your password
   - Enable 2FA
   - Remove suspicious apps
   - Review recent activity

3. **Report to Facebook:**
   - Use Facebook's "Report a Problem" feature
   - Mention specific dates/times of suspicious activity
   - Include IP addresses if available

4. **Consider professional help:**
   - Cybersecurity consultant
   - Law enforcement (if serious)
   - Legal counsel (if needed)

## Troubleshooting

### "No files found"
- Make sure files are in the `evidence/` directory
- Check file permissions

### "Error parsing JSON"
- Some Facebook JSON files may be malformed
- Try individual file analysis

### "PDF extraction failed"
- Install PDF libraries: `pip install PyPDF2 pdfplumber`
- Some PDFs may be image-based and need OCR

### Need more help?
Create an issue on GitHub with:
- What files you have
- What error you're seeing
- What you're trying to analyze

## Privacy Reminder

⚠️ **Never share:**
- Your actual Facebook data files
- The analysis reports containing personal info
- Screenshots with personal details

Keep this repository **private** and secure all outputs.
