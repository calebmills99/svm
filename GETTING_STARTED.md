# Getting Started - Quick Reference

## 🎯 What This Repository Does

This repository helps you analyze your Facebook data download to find evidence of the account breach that occurred around Christmas Eve 2024. It's specifically designed to help with your small claims court case against Meta.

---

## 📋 Prerequisites

✅ Python 3.6 or higher installed  
✅ Your Facebook data download from Meta (ZIP file)  
✅ Basic command line knowledge (or just follow the instructions!)  

---

## 🚀 Three Ways to Get Started

### Option 1: Quick Start (Easiest - Recommended)
```bash
./quickstart.sh
```
This interactive script will guide you through everything!

### Option 2: Step by Step
```bash
# 1. Verify you have your Facebook data ready
python3 check_data.py

# 2. Run the analysis
python3 analyze_breach.py

# 3. Review the reports
cat BREACH_REPORT.md
```

### Option 3: Read First, Then Run
1. Read `BREACH_ANALYSIS_GUIDE.md` for complete instructions
2. Upload your Facebook data to `facebook_data/` folder
3. Follow Option 1 or Option 2 above

---

## 📁 What You Need to Upload

1. **Download your Facebook data** from Meta if you haven't already
2. **Extract the ZIP file** - you'll get a folder with many subfolders
3. **Create a folder** called `facebook_data` in this repository
4. **Copy everything** from the extracted ZIP into `facebook_data/`

Your structure should look like:
```
svm/
├── facebook_data/           ← Your Facebook data goes here
│   ├── security_and_login_information/
│   ├── messages/
│   ├── posts/
│   └── ... (other folders)
├── analyze_breach.py
├── check_data.py
└── quickstart.sh
```

---

## 📊 What You'll Get

After running the analysis, you'll have:

1. **BREACH_REPORT.md** - Main findings report including:
   - Timeline of suspicious activities
   - List of suspicious IP addresses
   - Recommendations for your legal case

2. **timeline.txt** - Simple chronological list of events

3. **suspicious_ips.txt** - All IP addresses that accessed your account during the breach period

---

## 📝 Next Steps After Analysis

1. **Review the automated reports** - Start with `BREACH_REPORT.md`

2. **Fill out the investigation template**:
   - Open `INVESTIGATION_TEMPLATE.md`
   - Document your findings
   - Add your alibis and evidence

3. **Use the IOC checklist**:
   - Open `INDICATORS_OF_COMPROMISE.md`
   - Go through each item
   - Check off what you find

4. **Compile evidence for court**:
   - Organize all reports
   - Add supporting documents
   - Prepare your case

---

## 🔍 What the Analysis Looks For

- ✅ Logins from suspicious locations
- ✅ Unfamiliar devices accessing your account
- ✅ Activity at unusual times
- ✅ IP addresses from foreign countries
- ✅ Multiple locations in short time periods
- ✅ Account changes around the breach date

---

## 🛡️ Privacy & Security

- Your Facebook data stays on **your computer**
- Nothing is sent to the internet
- The `.gitignore` file protects your data from being committed to GitHub
- **Important**: Review your data before uploading to GitHub if you plan to push it

---

## ❓ Common Questions

**Q: I don't have my Facebook data yet. How do I get it?**  
A: See `BREACH_ANALYSIS_GUIDE.md` section "How to Get Your Facebook Data"

**Q: The analysis found nothing. Is that bad?**  
A: Not necessarily. The breach evidence might be in different files or formats. Review your data manually using the `INDICATORS_OF_COMPROMISE.md` checklist.

**Q: Can I see an example of what the report looks like?**  
A: Run the scripts with your data - the reports are in Markdown format and easy to read.

**Q: Is this legal/safe to use?**  
A: Yes! This analyzes YOUR data that Meta provided to you. It's for your personal investigation and legal case.

**Q: Do I need to be technical to use this?**  
A: No! Just run `./quickstart.sh` and follow the prompts.

---

## 📚 All Available Documents

| Document | Purpose |
|----------|---------|
| **README.md** | Project overview (you are here!) |
| **GETTING_STARTED.md** | This quick reference guide |
| **BREACH_ANALYSIS_GUIDE.md** | Complete step-by-step guide |
| **INDICATORS_OF_COMPROMISE.md** | Checklist of breach signs |
| **INVESTIGATION_TEMPLATE.md** | Template for documenting findings |

---

## 🆘 Need Help?

1. **Check the guides** - Most answers are in `BREACH_ANALYSIS_GUIDE.md`
2. **Review error messages** - They usually tell you what's wrong
3. **Create an issue** - Describe your problem in detail
4. **Check Python version** - Run `python3 --version` (need 3.6+)

---

## ⚖️ For Your Legal Case

This framework helps you:
- ✅ Document evidence chronologically
- ✅ Identify unauthorized access patterns
- ✅ Create professional reports for court
- ✅ Track suspicious IP addresses and locations
- ✅ Build a timeline of the breach

**Remember**: Keep all original files as evidence!

---

## 🎉 You're Ready!

Everything is set up and ready to go. Just add your Facebook data and run:

```bash
./quickstart.sh
```

Good luck with your investigation and legal case! 💪
