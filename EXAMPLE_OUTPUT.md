# Example Usage and Output

## What This Tool Does

This tool analyzes PDF files from Facebook/Meta for evidence of account breaches. Since no PDF file is currently in the repository, here's what will happen when you add one:

## Expected Workflow

### 1. You Add a PDF File

Place your Facebook data PDF in this directory. For example:
- `facebook_security_activity.pdf`
- `login_history.pdf`
- Any PDF from your Meta data download

### 2. Run the Analyzer

```bash
python pdf_analyzer.py facebook_security_activity.pdf
```

### 3. Tool Processes the PDF

The tool will:
- Extract all text from the PDF
- Search for security-related keywords
- Find IP addresses
- Identify location references
- Extract timestamps
- Analyze patterns of suspicious activity

### 4. Generates Three Output Files

**File 1: `facebook_security_activity_extracted_text.txt`**
```
--- Page 1 ---
Security Activity Report
Account: Caleb Stewart
Date: January 2026

Login History:
...
```

**File 2: `facebook_security_activity_analysis.json`**
```json
{
  "user_name": "Caleb Stewart",
  "analysis_date": "2026-01-11T20:30:00",
  "security_indicators": [
    {
      "keyword": "unauthorized",
      "context": "...detected unauthorized access from IP 192.168.1.1..."
    }
  ],
  "ip_addresses": ["192.168.1.1", "10.0.0.1"],
  "login_locations": ["Location: Moscow, Russia", "Location: New York, USA"],
  "key_findings": [
    "Found 15 security-related indicators in the document",
    "Identified 23 unique IP addresses"
  ]
}
```

**File 3: `facebook_security_activity_report.txt`**
```
================================================================================
FACEBOOK ACCOUNT BREACH EVIDENCE ANALYSIS REPORT
================================================================================

User: Caleb Stewart
Analysis Date: 2026-01-11T20:30:00

================================================================================

KEY FINDINGS:
--------------------------------------------------------------------------------
1. Found 15 security-related indicators in the document
2. Identified 23 unique IP addresses
3. Found 12 location references

SECURITY INDICATORS:
--------------------------------------------------------------------------------

'UNAUTHORIZED' (found 3 time(s)):
  Context: ...detected unauthorized access from IP 192.168.1.1 on Jan 5...
  Context: ...unauthorized password reset attempt...
  Context: ...unauthorized device login...

'SUSPICIOUS' (found 5 time(s)):
  Context: ...suspicious login activity detected...

IP ADDRESSES DETECTED:
--------------------------------------------------------------------------------
  - 192.168.1.1
  - 10.0.0.1
  - 203.45.67.89
  [... more IPs ...]

LOCATION REFERENCES:
--------------------------------------------------------------------------------
  - Location: Moscow, Russia
  - Location: New York, USA
  - Country: China
  [... more locations ...]

TIMESTAMPS FOUND:
--------------------------------------------------------------------------------
  - 01/05/2026
  - 01/10/2026
  - 12/15/2025
  [... more dates ...]

RECOMMENDATIONS:
--------------------------------------------------------------------------------
1. Review all IP addresses and verify if they match your known locations
2. Check timestamps for any activity during times when you were not active
3. Look for any unrecognized devices or login locations
4. Document all suspicious activities for potential legal/security reporting
5. Consider enabling two-factor authentication if not already enabled
6. Review and update security settings on all associated accounts

IMPLICATIONS:
--------------------------------------------------------------------------------
SECURITY BREACH EVIDENCE: This document may contain evidence of unauthorized
access to your Facebook account. The presence of security indicators suggests
that your account may have been compromised.

LEGAL CONSIDERATIONS: This evidence may be relevant for:
  - Filing a complaint with Meta/Facebook
  - Reporting to law enforcement or cybersecurity authorities
  - Identity theft protection services
  - Legal proceedings if damages occurred

IMMEDIATE ACTIONS: Consider taking the following steps:
  - Change passwords on all accounts (especially if reused)
  - Enable two-factor authentication
  - Review account activity and settings
  - Monitor credit reports for identity theft
  - Report the breach to appropriate authorities

DOCUMENTATION: Keep this analysis and the original PDF as evidence.
Consider consulting with a cybersecurity professional or attorney for
proper handling of this evidence.

================================================================================
END OF REPORT
================================================================================
```

## What the Analysis Tells You

### Security Indicators
Shows where security-related words appear in your PDF with surrounding context, helping you understand:
- What type of breach occurred
- When it was detected
- What actions were taken

### IP Addresses
Lists all IP addresses that accessed your account. You can:
- Look up each IP at https://www.iplocation.net/
- Compare with your known IP addresses (home, work, mobile)
- Identify foreign or suspicious IP addresses

### Location References
Shows where login attempts came from:
- If you see countries you've never visited → SUSPICIOUS
- If you see cities you weren't in on those dates → SUSPICIOUS
- Cross-reference with your travel history

### Timestamps
Dates and times help you:
- Identify when the breach occurred
- Correlate with your own activity
- Find patterns of unauthorized access
- Build a timeline for legal purposes

### Recommendations
Specific steps you should take to:
- Secure your account
- Protect your identity
- Prevent further damage
- Document evidence

### Implications
Explains:
- What the findings mean legally
- Where to report the breach
- What authorities to contact
- How to protect yourself

## Current Status

**No PDF file is in the repository yet.**

To use this tool:
1. Add your Facebook/Meta PDF file to this directory
2. Run: `python pdf_analyzer.py your_file.pdf`
3. Review the generated `*_report.txt` file

The tool is ready and waiting for your PDF file to analyze.

## Privacy Notice

⚠️ **IMPORTANT**: 
- The `.gitignore` file prevents PDF files and analysis results from being committed to git
- Your sensitive data will stay local on your machine
- Do not share the analysis files publicly as they contain personal information
- Keep all files secure for potential legal use
