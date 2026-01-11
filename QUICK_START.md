# Quick Start Guide for Caleb Stewart

## Immediate Steps to Analyze Your Facebook Breach Evidence

### Step 1: Prepare Your Environment

Open a terminal and navigate to this repository:

```bash
cd /path/to/svm
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Add Your PDF File

1. Locate the PDF file(s) from Meta/Facebook that contain evidence of the breach
2. Copy or move the PDF file into this repository directory
3. The file might be named something like:
   - `security_activity.pdf`
   - `login_history.pdf`
   - `account_activity.pdf`
   - Or any PDF from your Facebook data download

### Step 3: Run the Analysis

Run the analyzer script:

```bash
python pdf_analyzer.py your_facebook_file.pdf
```

Or simply:

```bash
python pdf_analyzer.py
```

The tool will automatically find and process PDF files.

### Step 4: Review the Results

The tool will create three files:

1. **Text Extract** (`*_extracted_text.txt`) - All text from the PDF
2. **JSON Data** (`*_analysis.json`) - Structured analysis data
3. **Report** (`*_report.txt`) - **START HERE** - Human-readable findings

Open the report file to see:
- Security indicators found
- IP addresses that accessed your account
- Locations of login attempts
- Timestamps of suspicious activity
- Recommendations for next steps
- Legal and security implications

### Step 5: What to Look For

When reviewing the report, pay attention to:

1. **Unrecognized IP Addresses**: IPs that don't match your home/work/mobile locations
2. **Suspicious Locations**: Logins from countries or cities you've never visited
3. **Unusual Timestamps**: Activity when you were asleep or not using Facebook
4. **Failed Login Attempts**: Multiple failed attempts might indicate hacking attempts
5. **Password Reset Events**: Unauthorized password changes
6. **Device Information**: Unrecognized devices accessing your account

### Step 6: Take Action

Based on the findings:

#### Immediate Security Actions:
- [ ] Change your Facebook password immediately
- [ ] Enable two-factor authentication on Facebook
- [ ] Review and remove any suspicious authorized apps
- [ ] Check for unrecognized devices in your Facebook security settings
- [ ] Change passwords on other accounts if you reused passwords
- [ ] Review your email account for unauthorized access

#### Documentation Actions:
- [ ] Save all generated files (text, JSON, report)
- [ ] Keep the original PDF file
- [ ] Take screenshots of suspicious activity in your Facebook account
- [ ] Document any financial losses or identity theft
- [ ] Create a timeline of when you noticed issues

#### Reporting Actions:
- [ ] Report to Facebook/Meta through their Help Center
- [ ] File a complaint with the FTC (ftc.gov/complaint)
- [ ] File a report with IC3 (ic3.gov) - FBI's Internet Crime Complaint Center
- [ ] Contact your local police department if identity theft occurred
- [ ] Alert your bank/credit card companies if financial info was exposed

#### Legal Actions (if needed):
- [ ] Consult with a lawyer specializing in cybersecurity or data breaches
- [ ] Consider identity theft protection services
- [ ] Review your rights under data protection laws

### Understanding the Output

**Security Indicators**: Keywords like "unauthorized", "suspicious", "breach" found in your Facebook data

**IP Addresses**: Every IP address that accessed your account. You can look these up at:
- https://www.whatismyip.com/ (to compare with your current IP)
- https://www.iplocation.net/ (to see geographic location of IPs)

**Timestamps**: When activities occurred - cross-reference with your own records

**Implications**: What the findings mean for your security and privacy

### Need Help Understanding the Technical Details?

The report includes:
- Plain English explanations of findings
- Context around each security indicator
- Specific recommendations for your situation
- Information about legal rights and options

### Important Reminders

1. **Keep Everything Confidential**: Don't share the PDF or reports publicly
2. **Preserve Evidence**: Keep all files in a safe, backed-up location
3. **Act Quickly**: The sooner you respond, the better you can protect yourself
4. **Document Everything**: Keep records of all actions you take
5. **Seek Professional Help**: Don't hesitate to consult experts

### What If No PDF Exists?

If you don't have a PDF yet:

1. **Download Your Facebook Data**:
   - Go to Facebook Settings
   - Click "Your Facebook Information"
   - Select "Download Your Information"
   - Choose "Security and Login Information"
   - Select PDF format
   - Download and save to this directory

2. **Request Security Information from Meta**:
   - Contact Meta Support
   - Request all security-related records
   - Ask specifically for breach notification documents

### Contact Information for Reporting

- **Meta/Facebook Help Center**: https://www.facebook.com/help
- **FTC Complaint**: https://ftc.gov/complaint
- **IC3 (FBI)**: https://www.ic3.gov
- **Identity Theft Resources**: https://www.identitytheft.gov

---

**Remember**: This is YOUR data and YOUR account. You have the right to know what happened and to take action to protect yourself.
