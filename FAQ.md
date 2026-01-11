# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is this repository for?

**A:** This repository contains tools to analyze Facebook data exports to help identify evidence of unauthorized account access or security breaches. It's specifically designed to help Caleb Stewart investigate a potential breach of his Facebook account.

### Q: Do I need to be a technical expert to use this?

**A:** No! The tools are designed to be user-friendly. You just need to:
1. Download your Facebook data
2. Put the files in the `evidence/` folder
3. Run the Python script
4. Read the generated report

### Q: Is this legal?

**A:** Yes! Analyzing **your own** Facebook data is completely legal. You own your data and have the right to analyze it.

### Q: Will this hack Facebook or access other people's accounts?

**A:** No! This tool **only** analyzes files you already have (your own Facebook data export). It doesn't access Facebook's systems or anyone else's data.

## Data & Privacy Questions

### Q: What data should I upload?

**A:** Upload the data archive that Facebook provides when you request "Download Your Information." This typically includes:
- Security and login information
- Account activity logs
- Messages
- Posts
- Apps and websites data

### Q: Is my data safe?

**A:** Your data stays on your computer or in your private GitHub repository. The tools run locally and don't send your data anywhere. **Important:** Make sure this repository is set to PRIVATE.

### Q: What if I accidentally made this repository public?

**A:** 
1. Immediately make it private (Settings → Danger Zone → Change visibility)
2. Delete any sensitive files from git history if they were committed
3. Consider the data potentially compromised and change your passwords

### Q: Should I commit my Facebook data files to GitHub?

**A:** **NO!** The `.gitignore` file is configured to exclude the `evidence/` directory and data files. Your personal data should never be committed to version control.

## Technical Questions

### Q: What programming language do I need to know?

**A:** You don't need to know any programming! Just run the Python scripts as shown in the documentation. Python is installed on most systems, or you can download it from python.org.

### Q: What if I don't have Python installed?

**A:** Download and install Python from [python.org](https://www.python.org/downloads/). Make sure to check "Add Python to PATH" during installation (Windows).

### Q: The script says "command not found" - what do I do?

**A:** 
- **Windows:** Use `py` instead of `python`: `py analyze_evidence.py`
- **Mac/Linux:** Make sure Python is installed: `python3 --version`
- Try: `python3 analyze_evidence.py` instead of `python analyze_evidence.py`

### Q: What if I get an import error?

**A:** Install the required libraries:
```bash
pip install -r requirements.txt
```

Or if that doesn't work:
```bash
pip3 install -r requirements.txt
```

### Q: Can I run this on Windows/Mac/Linux?

**A:** Yes! The tools are cross-platform and work on all major operating systems.

## Facebook Data Questions

### Q: How do I download my Facebook data?

**A:** 
1. Go to Facebook Settings (click the down arrow in top-right)
2. Click "Your Facebook Information"
3. Click "Download Your Information"
4. Select:
   - Date range: All time (or specific range)
   - Format: JSON or HTML (HTML is easier to read)
   - Media quality: Low (unless you need photos/videos)
5. Click "Create File"
6. Wait for email notification (can take hours or even days)
7. Download when ready

### Q: How long does Facebook take to prepare my data?

**A:** Usually a few hours to a few days, depending on how much data you have. Facebook will email you when it's ready.

### Q: What format should I choose - JSON or HTML?

**A:** Both work! 
- **HTML** is easier to read manually
- **JSON** is better for automated analysis
- You can request both if you want

### Q: My Facebook data is huge! Do I need all of it?

**A:** For breach analysis, the most important parts are:
- Security and login information
- Account activity
- Apps and websites
- Recent messages (if relevant to breach)

You don't necessarily need:
- Old photos and videos (unless investigating unauthorized uploads)
- Old posts (unless investigating unauthorized posting)

## Analysis Questions

### Q: What does the analysis tool look for?

**A:** The tool searches for:
- Logins from unknown locations or IP addresses
- Unrecognized devices
- Password or security setting changes
- Suspicious activity patterns
- Timeline anomalies
- Unauthorized app access

### Q: How do I know if something is suspicious?

**A:** The tool flags items as suspicious, but you should review them. Ask yourself:
- "Was this me?"
- "Do I recognize this location/IP/device?"
- "Was I traveling when this login occurred?"
- "Did I authorize this app?"

### Q: What if I get false positives?

**A:** False positives happen! Common causes:
- You logged in while traveling
- You used a VPN
- You logged in on a friend's device
- Your ISP's IP address changed
- You forgot you installed an app

Review each finding and use your judgment.

### Q: The report is very long - where should I focus?

**A:** Focus on:
1. **Critical section** - Most important findings
2. **Suspicious activities** - Potential security issues
3. **Logins from unknown locations** - Unauthorized access attempts
4. **Password changes** - Especially ones you didn't make

## Breach-Specific Questions

### Q: I found evidence of unauthorized access - what now?

**A:**
1. **Immediately** change your Facebook password
2. Enable two-factor authentication (2FA)
3. Review and remove suspicious apps
4. Log out of all sessions
5. Review recent activity and remove unauthorized content
6. Report to Facebook
7. Consider contacting law enforcement if serious
8. Consult with a cybersecurity professional if needed

### Q: Should I report this to the police?

**A:** If you have evidence of:
- Identity theft
- Financial loss
- Harassment or threats
- Other crimes committed using your account

Then yes, consider filing a police report. Bring:
- The analysis report
- Original Facebook data files
- Timeline of events
- Any other relevant evidence

### Q: Can this evidence be used in court?

**A:** Potentially, yes. To preserve evidence:
1. Don't modify the original files
2. Keep copies of everything
3. Document the chain of custody
4. Consult with a lawyer about proper evidence handling

### Q: Facebook says my account wasn't hacked, but I see suspicious activity. Why?

**A:** Facebook's automated systems may not catch everything. Common reasons:
- Sophisticated attacks that mimic normal behavior
- Session hijacking that doesn't trigger login alerts
- Cookie theft
- Social engineering attacks

Trust your analysis and evidence.

## Support Questions

### Q: I'm getting errors - where can I get help?

**A:** 
1. Check this FAQ first
2. Review the TROUBLESHOOTING section in EXAMPLES.md
3. Create a GitHub issue with:
   - The error message
   - What you were trying to do
   - Your operating system
   - Python version (`python --version`)

### Q: Can you analyze my data for me?

**A:** For privacy and security reasons, you should analyze your own data. The tools are designed to be easy to use even without technical expertise.

### Q: This is overwhelming - I need personal help!

**A:** Consider:
- Asking a tech-savvy friend to help
- Hiring a cybersecurity consultant
- Contacting a digital forensics professional
- Your local library may have tech help services

### Q: Can I modify these tools for my needs?

**A:** Yes! The code is open and you can customize it. If you're not a programmer, describe what you need in a GitHub issue.

## Next Steps

### Q: I've completed the analysis - what's next?

**A:** 
1. Review the entire report carefully
2. Save all evidence securely
3. Take immediate security actions
4. Report to Facebook if breach confirmed
5. Monitor your account for future suspicious activity
6. Consider enabling additional security features
7. Review other online accounts (email, banking, etc.)

### Q: How can I prevent future breaches?

**A:**
- Use strong, unique passwords for every account
- Enable two-factor authentication everywhere possible
- Be cautious about app permissions
- Don't click suspicious links
- Keep software updated
- Use a password manager
- Regularly review account security settings
- Be suspicious of phishing attempts

---

## Still have questions?

Create an issue on GitHub or add your question to this FAQ!
