# SVM - Security Verification & Monitoring

## Facebook Account Breach Investigation

This repository contains tools and documentation to help analyze Facebook data downloads for evidence of account breaches and unauthorized access.

### Background

This repository was created to investigate a Facebook account breach that occurred around Christmas Eve 2024. The account was subsequently disabled by Meta, and this analysis aims to identify evidence of the breach for legal proceedings.

### Quick Start

**Option 1: Automated Quick Start (Recommended)**
```bash
./quickstart.sh
```

**Option 2: Manual Steps**
1. **Read the Guide**: Start with [BREACH_ANALYSIS_GUIDE.md](BREACH_ANALYSIS_GUIDE.md) for complete instructions
2. **Upload Data**: Download your Facebook data and place it in a `facebook_data/` folder
3. **Verify Data**: Run `python3 check_data.py` to verify your data structure
4. **Run Analysis**: Execute `python3 analyze_breach.py`
5. **Review Report**: Check the generated `BREACH_REPORT.md` file

### What This Tool Does

The analysis tool (`analyze_breach.py`) examines your Facebook data to identify:

- ✅ Suspicious login locations
- ✅ Unusual login times
- ✅ Unfamiliar devices and IP addresses
- ✅ Account changes during the breach period
- ✅ Chronological timeline of events
- ✅ Indicators of unauthorized access

### Files in This Repository

**Analysis Tools**
- `analyze_breach.py` - Main analysis script for JSON data
- `check_data.py` - Validates Facebook data structure before analysis
- `quickstart.sh` - Interactive setup flow

**Documentation**
- `BREACH_ANALYSIS_GUIDE.md` - Complete step-by-step guide
- `GETTING_STARTED.md` - Quick reference for new users
- `INDICATORS_OF_COMPROMISE.md` - Checklist of breach indicators
- `INVESTIGATION_TEMPLATE.md` - Structured template for documenting findings

### Generated Reports

After running the analysis, you'll get:

- `BREACH_REPORT.md` - Detailed findings and recommendations
- `timeline.txt` - Chronological event timeline
- `suspicious_ips.txt` - List of suspicious IP addresses

### Privacy & Security

⚠️ **Important**: Before uploading your Facebook data to GitHub:

1. Review all files for personal information
2. Consider keeping the repository private
3. Redact sensitive information (messages, phone numbers, etc.)
4. See the guide for detailed privacy recommendations

### Requirements

- Python 3.6 or higher
- Your Facebook data download (JSON format)

### Usage

**Quick Start (Easiest):**
```bash
# Clone this repository
git clone https://github.com/calebmills99/svm.git
cd svm

# Add your Facebook data to facebook_data/ folder
mkdir facebook_data
# ... copy your Facebook data here ...

# Run the guided quick start
./quickstart.sh
```

**Manual Usage:**
```bash
# Verify your data structure
python3 check_data.py

# Run the analysis
python3 analyze_breach.py

# Review the results
cat BREACH_REPORT.md
cat timeline.txt
cat suspicious_ips.txt
```

### For Legal Proceedings

This tool helps create a documented record of:

- When the breach occurred
- What unauthorized activities took place
- IP addresses and locations of attackers
- Timeline of events for court evidence

All generated reports are formatted to be clear and presentable for legal review.

### Need Help?

If you need assistance:

1. Check the [BREACH_ANALYSIS_GUIDE.md](BREACH_ANALYSIS_GUIDE.md)
2. Ensure your Facebook data is properly extracted
3. Verify Python 3 is installed: `python3 --version`
4. Create an issue in this repository with details

### Contributing

This tool was created to help analyze a specific breach case but can be useful for others investigating Facebook account compromises. Contributions to improve the analysis capabilities are welcome.

### License

This tool is provided as-is for personal use in investigating account security incidents.

### Disclaimer

This tool is designed to help analyze and document Facebook data downloads. It does not guarantee finding all evidence of a breach and should be used as part of a comprehensive security investigation. For legal matters, consult with appropriate legal counsel.
