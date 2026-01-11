# Facebook Account Breach Evidence Analysis Toolkit

This repository contains comprehensive tools to analyze data downloaded from Meta/Facebook to investigate potential account breaches or unauthorized access.

## Overview

This toolkit is designed to help **Caleb Stewart** analyze Facebook/Meta data downloads that contain evidence of account security breaches. It includes multiple analysis tools that can parse PDF files, HTML exports, and JSON data to extract relevant security information and generate detailed reports with implications and recommendations.

## 🚨 Important: Data Files Required

**To use these analysis tools, you need to:**

1. **Download your Facebook data** from Meta/Facebook (Settings → Your Facebook Information → Download Your Information)
2. **Extract and place the files** in this repository
3. **Run the appropriate analysis** tool

## 📖 Documentation

**New here?** See **[INDEX.md](INDEX.md)** for a complete guide to all documentation.

Quick links:
- **[QUICKSTART.md](QUICKSTART.md)** - Quick setup guide (5 minutes)
- **[QUICK_START.md](QUICK_START.md)** - PDF analyzer quick start
- **[CHECKLIST.md](CHECKLIST.md)** - Complete investigation checklist
- **[FAQ.md](FAQ.md)** - Frequently asked questions
- **[EXAMPLES.md](EXAMPLES.md)** - Usage examples
- **[EXAMPLE_OUTPUT.md](EXAMPLE_OUTPUT.md)** - Sample output from PDF analyzer

## Analysis Tools

This repository includes three complementary analysis tools:

### 1. PDF Analyzer (`pdf_analyzer.py`)
Specialized tool for analyzing PDF files from Facebook/Meta:
- Extracts text content from PDF files
- Identifies security indicators and suspicious activities
- Detects IP addresses, locations, and timestamps
- Generates detailed reports with implications

**Usage:**
```bash
python pdf_analyzer.py your_facebook_data.pdf
```

### 2. Multi-Format Evidence Analyzer (`analyze_evidence.py`)
Comprehensive tool that analyzes multiple file formats:
- Parses JSON, HTML, and PDF files
- Extracts login history, IP addresses, devices, security events
- Generates human-readable breach reports
- Works with complete Facebook data exports

**Usage:**
```bash
# Install dependencies
pip install -r requirements.txt

# Download Facebook data from Meta, extract to evidence/
mkdir -p evidence
cp -r facebook-download/* evidence/

# Run analysis
python analyze_evidence.py
```

### 3. Facebook HTML Parser (`parse_facebook_html.py`)
Specialized parser for Facebook's HTML security exports:
- Extracts structured login data
- Parses security events and IP addresses
- Identifies suspicious activity patterns

**Usage:**
```bash
python parse_facebook_html.py evidence/security_and_login_information.html
```

## Installation

1. Clone this repository (or you already have it)
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## What Gets Analyzed

All tools search for and analyze:

- ✅ Login history and locations
- ✅ IP addresses used to access the account
- ✅ Device information
- ✅ Security events (password changes, 2FA changes, etc.)
- ✅ Suspicious activities and patterns
- ✅ Timeline of events
- ✅ Unauthorized access indicators
- ✅ Session data and authentication events

## Output Files

Depending on which tool you use:

### PDF Analyzer Output:
- `*_extracted_text.txt`: Raw text extracted from the PDF
- `*_analysis.json`: Structured analysis data in JSON format
- `*_report.txt`: Human-readable detailed report

### Evidence Analyzer Output:
- `analysis_report.txt`: Comprehensive report with suspicious activities and unauthorized access indicators

## Privacy & Security

⚠️ **KEEP THIS REPOSITORY PRIVATE** if it contains your personal data!

Your Facebook data may include highly sensitive information:
- Private messages and conversations
- Contact information and relationships
- Location history
- Financial information
- Photos and videos

The `.gitignore` file is configured to exclude personal data files, and all processing is done locally on your computer.

## For Caleb Stewart

This toolkit was created to help you analyze your Facebook data export files containing evidence of potential account breaches. You can use:

1. **`pdf_analyzer.py`** - If you have PDF files with security information
2. **`analyze_evidence.py`** - If you have a complete Facebook data export (JSON/HTML)
3. **Both tools** - For comprehensive analysis of all file types

Once you upload your files, the analysis tools will:
1. Parse all PDFs, HTML, and JSON files
2. Extract security-relevant information
3. Identify suspicious activities
4. Generate comprehensive reports

## Report Sections

The generated reports include:

1. **Key Findings / Summary**: High-level summary of detected issues
2. **Suspicious Activities**: Specific security concerns identified
3. **Security Indicators**: Security-related keywords and their context
4. **Detailed Findings**: Complete analysis of all extracted data
5. **IP Addresses**: List of all detected IP addresses
6. **Location References**: Geographic locations found
7. **Timestamps**: Chronological data points
8. **Recommendations**: Actionable steps for security improvement
9. **Implications**: Legal, security, and practical implications

## Important Notes

### Privacy
- Your data stays on your computer - no information is sent externally
- Make sure this repository is set to **PRIVATE** if on GitHub
- Never share analysis reports containing personal information

### Legal Considerations
- This tool analyzes **your own** data for security purposes
- Results may be used as evidence if needed
- Consider consulting with:
  - Cybersecurity professionals
  - Legal counsel
  - Law enforcement (if criminal activity is suspected)

### Data Integrity
- Keep original files unmodified
- Save multiple copies of analysis results
- Document the chain of custody for legal purposes

## Legal Notice

This tool is for analyzing **your own** Facebook data for security purposes. If you believe your account was breached:
- Contact Meta/Facebook support immediately
- Change your passwords and enable two-factor authentication
- Review and revoke access to suspicious apps
- Consider consulting with a cybersecurity professional
- Consult with legal counsel if needed
- Report to law enforcement if criminal activity is suspected

## Troubleshooting

See [FAQ.md](FAQ.md) for common questions and issues, including:
- Installation problems
- File format issues
- Understanding analysis results
- What to do if you find evidence of a breach

## Additional Resources

- **Facebook Help Center**: https://www.facebook.com/help
- **How to download your Facebook data**: Settings → Your Facebook Information → Download Your Information
- **FBI Internet Crime Complaint Center**: https://www.ic3.gov
- **FTC Identity Theft Resources**: https://identitytheft.gov
