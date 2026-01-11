# Quick Start Guide

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Evidence Directory

```bash
mkdir -p evidence/{pdfs,html,data,other}
```

### 3. Upload Your Files

Place your Facebook data files in the evidence directory:
- PDF files → `evidence/pdfs/`
- HTML files → `evidence/html/`
- JSON files → `evidence/data/`
- Other files → `evidence/other/`

Or simply place all files in the `evidence/` directory, and the analyzer will categorize them automatically.

### 4. Run the Analysis

```bash
python analyze_evidence.py
```

Or specify a custom directory:

```bash
python analyze_evidence.py --evidence-dir /path/to/your/files --output my_report.txt
```

## What Gets Analyzed

The script will:

1. **Scan** all files in the evidence directory
2. **Parse** JSON and HTML files for security-related information
3. **Identify** suspicious keywords and activities
4. **Extract** login history, IP addresses, and security events
5. **Generate** a comprehensive report

## Understanding Your Facebook Data

When you download your Facebook data, you typically get:

### Security & Login Information
- `security_and_login_information.html` - Login history
- `account_activity.json` - Account changes and activities
- `security_and_login_information/` folder

### Messages
- `messages/` folder with JSON or HTML files
- `your_posts/` folder

### Activity
- `posts/` folder
- `comments/` folder
- `likes_and_reactions/` folder

### Apps and Websites
- `apps_and_websites/` folder
- Shows what apps had access to your account

## Looking for Evidence of Breach

The analyzer looks for:

### 🔴 Critical Indicators
- Unrecognized login locations
- Unknown IP addresses
- Devices you don't recognize
- Password changes you didn't make
- Login attempts from suspicious locations

### 🟡 Warning Signs
- Unusual activity times
- Messages you didn't send
- Posts you didn't make
- Friends you didn't add
- Apps you didn't authorize

### 🟢 Normal Activity
- Your regular login locations
- Your known devices
- Your actual posts and messages

## Next Steps After Analysis

1. **Review the Report** - Read `analysis_report.txt` carefully
2. **Document Everything** - Save all evidence
3. **Secure Your Account** - Change passwords, enable 2FA
4. **Report to Facebook** - Contact Meta support
5. **Consider Legal Action** - If needed, consult an attorney

## Need More Help?

- Check `ANALYSIS_README.md` for detailed information
- Create a GitHub issue if you encounter problems
- Include the type of files you have and any errors

## Privacy Warning

⚠️ **Keep this repository PRIVATE** if it contains your personal Facebook data!

Your Facebook data may include:
- Private messages
- Photos and videos
- Contact information
- Financial data
- Location history

Never share this publicly!
