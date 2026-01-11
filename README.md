# SVM - Security Breach Evidence Analyzer

This repository contains tools to analyze PDF files from Facebook/Meta containing evidence of potential account breaches and unauthorized access.

## Overview

This tool is designed to help **Caleb Stewart** analyze Facebook/Meta data downloads that contain evidence of account security breaches. It parses PDF files, extracts relevant security information, and generates detailed reports with implications and recommendations.

## Features

- **PDF Text Extraction**: Extracts text content from PDF files
- **Security Analysis**: Identifies security indicators, suspicious activities, and breach evidence
- **IP Address Detection**: Finds and lists all IP addresses mentioned in the document
- **Location Tracking**: Extracts geographic location references
- **Timestamp Analysis**: Identifies dates and times of activities
- **Comprehensive Reporting**: Generates detailed reports with findings and implications
- **Actionable Recommendations**: Provides next steps for security and legal considerations

## Installation

1. Clone this repository (or you already have it)
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

1. Place your Facebook/Meta PDF file(s) in the repository directory
2. Run the analyzer:

```bash
python pdf_analyzer.py
```

This will automatically process the first PDF file found in the directory.

### Specify a PDF File

To analyze a specific PDF file:

```bash
python pdf_analyzer.py your_facebook_data.pdf
```

### Output Files

The analyzer generates three output files for each PDF processed:

1. **`*_extracted_text.txt`**: Raw text extracted from the PDF
2. **`*_analysis.json`**: Structured analysis data in JSON format
3. **`*_report.txt`**: Human-readable detailed report with findings and implications

## What the Tool Analyzes

The tool searches for and analyzes:

- **Security Keywords**: unauthorized access, breach, compromise, suspicious activity, etc.
- **IP Addresses**: All IP addresses mentioned in the document
- **Login Locations**: Geographic locations associated with account access
- **Timestamps**: Dates and times of activities
- **Device Information**: Information about devices used to access the account
- **Session Data**: Login sessions and authentication events

## Report Sections

The generated report includes:

1. **Key Findings**: High-level summary of detected issues
2. **Security Indicators**: Specific security-related keywords and their context
3. **IP Addresses**: List of all detected IP addresses
4. **Location References**: Geographic locations found in the document
5. **Timestamps**: Chronological data points
6. **Recommendations**: Actionable steps for security improvement
7. **Implications**: Legal, security, and practical implications of the findings

## Important Notes

### For Caleb Stewart

This tool is specifically configured for analyzing your Facebook/Meta account breach evidence. The analysis includes:

- Evidence of unauthorized access to your account
- Potential indicators of hacking or compromise
- Documentation suitable for legal or security reporting purposes
- Recommendations for protecting your identity and accounts

### Legal and Security Considerations

- **Keep the Original Files**: Preserve all original PDF files as evidence
- **Document Everything**: The generated reports can be used for legal purposes
- **Consult Professionals**: Consider consulting with:
  - Cybersecurity professionals for technical analysis
  - Attorneys for legal advice
  - Law enforcement for criminal matters
  - Identity theft protection services
- **Report to Authorities**: Consider filing reports with:
  - Meta/Facebook support
  - Local law enforcement
  - Federal Trade Commission (FTC)
  - Internet Crime Complaint Center (IC3)

### Privacy and Security

- Do not share the PDF files or reports publicly as they may contain sensitive personal information
- Store analysis results securely
- Consider the files contain evidence and handle them appropriately

## Troubleshooting

### PDF Library Issues

If you encounter errors related to PDF parsing, try:

1. Ensure requirements are installed: `pip install -r requirements.txt`
2. Try updating the libraries: `pip install --upgrade PyPDF2 pdfplumber`
3. If one library fails, the tool will automatically try the alternative

### No PDF Files Found

Make sure:
1. PDF files are in the same directory as `pdf_analyzer.py`
2. Files have the `.pdf` extension
3. You have read permissions on the files

## Example Workflow

1. Download your Facebook data from Meta (Settings > Your Facebook Information > Download Your Information)
2. Extract any PDF files containing security or login information
3. Place the PDF in this repository folder
4. Run: `python pdf_analyzer.py facebook_security_data.pdf`
5. Review the generated `*_report.txt` file for findings
6. Follow the recommendations in the report
7. Keep all files as evidence if needed for legal purposes

## Support

This tool is designed for personal use to analyze account breach evidence. For technical issues or questions, review the code or modify as needed for your specific use case.

## License

This tool is provided as-is for personal security analysis purposes.