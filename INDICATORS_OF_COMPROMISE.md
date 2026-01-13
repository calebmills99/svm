# Facebook Account Breach - Indicators of Compromise (IOCs)

## What to Look For in Your Facebook Data

This checklist helps you identify evidence of unauthorized access to your Facebook account.

## Timeline Context
- **Breach Date**: Christmas Eve 2024 (December 24, 2024)
- **Investigation Period**: 2-3 weeks before and after the breach date
- **Account Status**: Disabled by Meta

---

## 🔐 Login and Access Indicators

### Suspicious Login Patterns
- [ ] Logins from countries/cities you've never visited
- [ ] Multiple logins from different countries within hours
- [ ] Logins at unusual times (e.g., 3 AM when you're always asleep)
- [ ] Logins from VPN/proxy IP addresses
- [ ] Concurrent sessions from impossible locations (e.g., USA and China simultaneously)

### Device Indicators
- [ ] Unknown devices in "Where You're Logged In"
- [ ] Operating systems you don't use (e.g., Android when you only use iPhone)
- [ ] Browsers you don't use
- [ ] Multiple new device authorizations around the breach date

### IP Address Red Flags
- [ ] IP addresses from foreign countries
- [ ] IP addresses from hosting providers/data centers (not residential)
- [ ] IPs from known VPN providers
- [ ] Multiple different IPs in short time periods

---

## 📝 Account Changes

### Security Settings
- [ ] Password changed (check for change notifications you didn't make)
- [ ] Email address changed or added
- [ ] Phone number changed or removed
- [ ] Two-factor authentication disabled
- [ ] Recovery options modified
- [ ] Security questions changed

### Profile Changes
- [ ] Profile picture changed
- [ ] Cover photo changed
- [ ] Bio/about information modified
- [ ] Contact information altered
- [ ] Privacy settings changed

---

## 💬 Content and Activity

### Posts and Content
- [ ] Posts you didn't create
- [ ] Shared content you don't remember sharing
- [ ] Comments made in your name
- [ ] Reactions/likes on posts you didn't interact with
- [ ] Photos/videos uploaded that you didn't upload

### Messages
- [ ] Messages sent to people you didn't contact
- [ ] Messages in languages you don't speak
- [ ] Spam or scam messages sent from your account
- [ ] Friend requests sent to unknown people
- [ ] Group messages you didn't join

### Friend Activity
- [ ] Friends added you don't know
- [ ] Friends removed without your action
- [ ] Bulk friend requests sent
- [ ] Messages asking your friends for money

---

## 🔧 Apps and Integrations

### Connected Apps
- [ ] Unknown apps with access to your account
- [ ] Apps authorized around the breach date
- [ ] Apps with suspicious permissions (post on your behalf, access messages, etc.)
- [ ] Games or services you don't recognize

### Third-Party Access
- [ ] Instagram/WhatsApp connections changed
- [ ] Other Meta product linkages modified
- [ ] Business accounts created or linked

---

## 🚨 High-Priority Evidence

### Critical Indicators (Strong Evidence of Breach)
1. **Geographic Impossibility**: Logins from two different continents within hours
2. **Concurrent Sessions**: Active sessions in multiple countries at the same time
3. **Mass Actions**: Bulk friend requests, mass messages, many posts in short time
4. **Financial Attempts**: Messages requesting money, sharing payment scams
5. **Account Lockout**: Password changes that locked you out
6. **Recovery Attacks**: Multiple password reset attempts

### Documentation Needed
For each suspicious activity, document:
- **What**: Exactly what happened
- **When**: Precise date and time
- **Where**: Location/IP address
- **Impact**: What damage or access was lost
- **Evidence**: Screenshot, file reference, log entry

---

## 📊 Analysis Patterns

### Patterns That Suggest Breach
1. **Activity Spike**: Sudden increase in activity around December 24, 2024
2. **Location Shift**: Regular login pattern changes to foreign locations
3. **Behavioral Changes**: Activity patterns don't match your normal usage
4. **Time Zone Anomalies**: Active when you're typically asleep
5. **Language Indicators**: Content in languages you don't speak

### Legitimate vs. Suspicious
Compare suspicious activity against:
- Your actual location history (phone GPS, calendar, credit card statements)
- Your typical online activity hours
- Your known devices and IP addresses
- Your travel history

---

## 🎯 For Your Legal Case

### Evidence to Compile
1. **Timeline Document**: Chronological list of all unauthorized activities
2. **IP Address List**: All suspicious IPs with geolocation
3. **Content Screenshots**: Posts, messages, changes you didn't make
4. **Access Log**: When you were locked out vs. unauthorized access times
5. **Damage Documentation**: What you lost access to, any financial impact
6. **Meta Communications**: Any emails or notifications from Facebook/Meta

### Proving Unauthorized Access
Strong evidence includes:
- Activity while you have an alibi (at work, photos prove different location)
- Technical impossibility (two places at once)
- Content you couldn't have created (wrong language, knowledge you don't have)
- Pattern breaks (sudden change from years of normal behavior)

---

## 📋 Checklist for Investigation

### Phase 1: Initial Review
- [ ] Run `python3 check_data.py` to verify data structure
- [ ] Run `python3 analyze_breach.py` to generate reports
- [ ] Review BREACH_REPORT.md for automated findings
- [ ] Read through timeline.txt chronologically

### Phase 2: Manual Investigation
- [ ] Check each suspicious IP in timeline against your known locations
- [ ] Review login devices - mark known vs. unknown
- [ ] Look through posts/messages for content you didn't create
- [ ] Check for account changes (email, password, phone)
- [ ] Review connected apps for unauthorized additions

### Phase 3: Evidence Compilation
- [ ] Create list of unauthorized activities with timestamps
- [ ] Document your actual whereabouts during suspicious logins
- [ ] Screenshot or save examples of unauthorized content
- [ ] List all damage/impact (locked out, data lost, reputation harm)
- [ ] Organize for legal presentation

### Phase 4: Documentation for Court
- [ ] Create executive summary of the breach
- [ ] Prepare evidence binder with timeline
- [ ] Document financial impact (if any)
- [ ] Include Meta's response (or lack thereof)
- [ ] Summarize security failures by Meta

---

## 🔍 Additional Resources

### Checking IP Addresses
You can look up IP addresses to see their location and owner:
- https://www.iplocation.net/
- https://whatismyipaddress.com/ip-lookup
- Look for: Country, City, ISP/Organization, Type (residential vs. hosting)

### Understanding Facebook's Responsibility
For your legal case, consider:
- Did Meta fail to detect obvious breach indicators?
- Were you notified of suspicious activity?
- Did Meta provide adequate security features?
- Was their response to the breach appropriate?
- Did they disable your account unfairly?

---

## ⚠️ Important Notes

1. **Preserve Everything**: Don't delete any data, even if it seems unimportant
2. **Multiple Copies**: Keep backups of the Facebook data download
3. **Document Now**: Memories fade - write down everything you remember
4. **Timeline is Key**: Precise dates and times are critical for legal cases
5. **Be Objective**: Let the evidence speak - avoid speculation in official docs

---

## Next Steps

After reviewing this checklist:

1. Work through each section systematically
2. Mark items you find evidence for
3. Add notes and details to each checked item
4. Compile your findings into a summary document
5. Consult with legal counsel about your case

Remember: The goal is to build a clear, evidence-based case showing:
- Your account was breached
- Unauthorized access occurred
- Meta failed to protect you or respond appropriately
- You suffered damages as a result
