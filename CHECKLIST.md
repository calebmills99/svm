# Account Breach Investigation Checklist

Use this checklist to guide your investigation and response.

## Phase 1: Preparation ⚙️

- [ ] Clone or download this repository
- [ ] Install Python (if not already installed)
- [ ] Install required libraries: `pip install -r requirements.txt`
- [ ] Create the evidence directory: `mkdir evidence`
- [ ] Ensure this repository is set to PRIVATE (if on GitHub)

## Phase 2: Data Collection 📥

- [ ] Request Facebook data download
  - [ ] Go to Facebook Settings → Your Facebook Information
  - [ ] Click "Download Your Information"
  - [ ] Select date range (recommend: All time)
  - [ ] Select format (recommend: JSON or HTML)
  - [ ] Click "Create File"
  
- [ ] Wait for Facebook notification email (this can take hours or days)

- [ ] Download the data archive when ready

- [ ] Extract the archive
  - [ ] Unzip the downloaded file
  - [ ] Move files to the `evidence/` directory in this repository

- [ ] Verify you have these important files/folders:
  - [ ] security_and_login_information/
  - [ ] account_activity/
  - [ ] apps_and_websites/
  - [ ] messages/ (if relevant)
  - [ ] your_posts/ (if investigating unauthorized posting)

## Phase 3: Analysis 🔍

- [ ] Run the main analysis tool:
  ```bash
  python analyze_evidence.py
  ```

- [ ] Run specialized HTML parser (if you have HTML files):
  ```bash
  python parse_facebook_html.py evidence/security_and_login_information.html
  ```

- [ ] Review the generated report: `analysis_report.txt`

- [ ] Document your findings:
  - [ ] List all suspicious IP addresses
  - [ ] List all unrecognized devices
  - [ ] Note dates/times of suspicious activity
  - [ ] Identify any unauthorized changes to your account

## Phase 4: Evidence Review 📋

Go through the report section by section:

### Login History
- [ ] Review all login locations - do you recognize them all?
- [ ] Check login times - do they match your schedule?
- [ ] Verify devices - are they all yours?
- [ ] Check IP addresses - are they from your ISP or locations you've been?

### Security Events
- [ ] Review password changes - did you make them all?
- [ ] Check email/phone changes - are they legitimate?
- [ ] Verify 2FA settings - any unauthorized changes?
- [ ] Review recovery options - any suspicious additions?

### Account Activity
- [ ] Check posts - did you make them all?
- [ ] Review messages - any you don't remember sending?
- [ ] Verify friend requests - did you send them?
- [ ] Check profile changes - are they your changes?

### Apps and Websites
- [ ] List all connected apps
- [ ] Mark any apps you don't recognize
- [ ] Check permissions granted to each app
- [ ] Note any suspicious data access

## Phase 5: Immediate Response 🚨

If you found evidence of unauthorized access:

### Secure Your Account
- [ ] Change your Facebook password immediately
  - [ ] Use a strong, unique password
  - [ ] Don't reuse passwords from other accounts
  
- [ ] Enable two-factor authentication (2FA)
  - [ ] Set up authentication app (not SMS if possible)
  - [ ] Save backup codes in a secure location

- [ ] Log out of all sessions
  - [ ] Go to Settings → Security → Where You're Logged In
  - [ ] Click "Log Out Of All Sessions"

- [ ] Remove suspicious apps
  - [ ] Go to Settings → Apps and Websites
  - [ ] Remove any apps you don't recognize or trust

- [ ] Review and update recovery information
  - [ ] Verify email addresses
  - [ ] Verify phone numbers
  - [ ] Remove any unauthorized recovery options

### Check Related Accounts
- [ ] Change password on your email account (used for Facebook)
- [ ] Check your email for unauthorized password reset requests
- [ ] Review other social media accounts
- [ ] Check your financial accounts if linked to Facebook
- [ ] Review any apps that use "Login with Facebook"

## Phase 6: Reporting 📢

### Report to Facebook
- [ ] Report the breach to Facebook
  - [ ] Go to Settings → Security and Login
  - [ ] Look for "Report Compromised Account" or similar
  - [ ] Follow Facebook's account recovery process
  
- [ ] Document what you report:
  - [ ] Date and time of report
  - [ ] What you reported
  - [ ] Any reference numbers given

### Report to Authorities (if applicable)
Consider reporting if:
- [ ] Financial loss occurred
- [ ] Identity theft is suspected
- [ ] Crimes were committed using your account
- [ ] You were threatened or harassed

If yes:
- [ ] File a report with local law enforcement
- [ ] File a report with FBI IC3 (if in US): https://www.ic3.gov
- [ ] Contact FTC (if identity theft): https://identitytheft.gov
- [ ] Keep copies of all police reports

### Notify Others (if needed)
- [ ] Warn friends/contacts if spam was sent from your account
- [ ] Notify family members (in case hackers try to scam them)
- [ ] Alert employer if work-related information was accessed
- [ ] Notify financial institutions if relevant

## Phase 7: Documentation 📁

Create a comprehensive evidence package:

- [ ] Save all analysis reports
- [ ] Take screenshots of suspicious activities in Facebook
- [ ] Export the original Facebook data files to a secure backup
- [ ] Create a timeline document with:
  - [ ] Date/time of first suspicious activity
  - [ ] Date/time when you discovered the breach
  - [ ] All suspicious events in chronological order
  - [ ] Actions you've taken
  
- [ ] Organize evidence by:
  - [ ] Suspicious logins (with IP addresses, locations, devices)
  - [ ] Unauthorized changes (password, email, settings)
  - [ ] Unauthorized activity (posts, messages, friend requests)
  - [ ] Malicious apps or permissions
  
- [ ] Store all evidence securely:
  - [ ] Create encrypted backup
  - [ ] Store in multiple locations
  - [ ] Don't delete original files

## Phase 8: Professional Consultation 👥

Consider consulting professionals if:

- [ ] The breach is sophisticated or ongoing
- [ ] Financial loss has occurred
- [ ] You need evidence for legal proceedings
- [ ] You're not confident in your analysis

Professionals to consider:
- [ ] Cybersecurity consultant or digital forensics expert
- [ ] Attorney (especially if pursuing legal action)
- [ ] Law enforcement cyber crimes unit
- [ ] Your employer's IT security team (if work-related)

## Phase 9: Ongoing Monitoring 🔄

After the immediate response:

### Week 1
- [ ] Check Facebook daily for suspicious activity
- [ ] Monitor email for unauthorized login attempts
- [ ] Review connected apps weekly
- [ ] Check for any new unauthorized posts/messages

### Month 1
- [ ] Review login locations weekly
- [ ] Check for new unrecognized devices
- [ ] Verify security settings haven't changed
- [ ] Monitor credit reports (if identity theft suspected)

### Ongoing
- [ ] Review account security monthly
- [ ] Update passwords every 3-6 months
- [ ] Keep 2FA enabled
- [ ] Stay alert for phishing attempts
- [ ] Review connected apps quarterly

## Phase 10: Prevention 🛡️

Prevent future breaches:

- [ ] Use a password manager
- [ ] Create unique passwords for every account
- [ ] Enable 2FA on all accounts that support it
- [ ] Regularly review account security settings
- [ ] Be cautious about:
  - [ ] Clicking links in emails/messages
  - [ ] Downloading attachments
  - [ ] Granting app permissions
  - [ ] Public Wi-Fi usage (use VPN)
- [ ] Keep software and devices updated
- [ ] Use antivirus/anti-malware software
- [ ] Educate yourself about common scams
- [ ] Trust your instincts - if something seems off, investigate

## Additional Resources 📚

- [ ] Review Facebook's Security Help Center
- [ ] Read about common hacking methods
- [ ] Learn about phishing and social engineering
- [ ] Consider cybersecurity training/courses
- [ ] Join online security communities for tips

---

## Notes Section

Use this space to track important information:

**Date breach discovered:** _______________

**Estimated date of breach:** _______________

**Most suspicious IP address(es):** 
- _______________
- _______________

**Unrecognized devices:**
- _______________
- _______________

**Unauthorized changes made:**
- _______________
- _______________

**Police report number (if filed):** _______________

**Facebook case number (if any):** _______________

**Additional notes:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

---

**Remember:** Work through this checklist systematically. Don't skip steps, especially in securing your account and documenting evidence.

**Status:**
- [ ] Investigation complete
- [ ] Account secured
- [ ] Evidence documented
- [ ] Reports filed (if applicable)
- [ ] Ongoing monitoring in place
