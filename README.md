# Facebook Account Breach Evidence Analysis Tool

This repository contains tools to help analyze data downloaded from Meta/Facebook to investigate potential account breaches or unauthorized access.

## 🚨 Important: Data Files Required

**Currently, no data files are present in this repository.** To use these analysis tools, you need to:

1. **Download your Facebook data** from Meta/Facebook
2. **Upload the files** to this repository
3. **Run the analysis** tools

## Quick Start

See **[QUICKSTART.md](QUICKSTART.md)** for step-by-step instructions.

## What's Included

- **`analyze_evidence.py`** - Main analysis script for all file types
- **`parse_facebook_html.py`** - Specialized HTML parser for Facebook security files
- **`ANALYSIS_README.md`** - Detailed documentation
- **`requirements.txt`** - Python dependencies

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create evidence directory and add your files:
   ```bash
   mkdir -p evidence
   # Copy your Facebook data files to the evidence/ directory
   ```

3. Run analysis:
   ```bash
   python analyze_evidence.py
   ```

4. Review the generated report: `analysis_report.txt`

## What Gets Analyzed

- ✅ Login history and locations
- ✅ IP addresses used to access your account
- ✅ Device information
- ✅ Security events (password changes, 2FA changes, etc.)
- ✅ Suspicious activities
- ✅ Timeline of events
- ✅ Unauthorized access indicators

## Privacy & Security

⚠️ **KEEP THIS REPOSITORY PRIVATE** if it contains your personal data!

Your Facebook data may include sensitive information. See `ANALYSIS_README.md` for privacy considerations.

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Quick setup guide
- **[ANALYSIS_README.md](ANALYSIS_README.md)** - Detailed analysis documentation

## For Caleb Stewart

This tool was created to help you analyze your Facebook data export files. The files should contain evidence related to the account breach you mentioned.

Once you upload your files, the analysis tools will:
1. Parse all PDFs, HTML, and JSON files
2. Extract security-relevant information
3. Identify suspicious activities
4. Generate a comprehensive report

## Legal Notice

This tool is for analyzing **your own** Facebook data for security purposes. If you believe your account was breached, consider:
- Contacting Meta/Facebook support
- Consulting with a cybersecurity professional
- Consulting with legal counsel if needed