#!/bin/bash
# Quick Start Helper Script for Facebook Breach Analysis
# This script helps guide you through the analysis process

echo "==========================================================="
echo "  Facebook Account Breach Investigation - Quick Start"
echo "==========================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3 to continue."
    exit 1
fi

echo "✅ Python 3 is installed: $(python3 --version)"
echo ""

# Check if facebook_data directory exists
if [ ! -d "facebook_data" ]; then
    echo "📋 STEP 1: Upload Your Facebook Data"
    echo "-----------------------------------------------------------"
    echo ""
    echo "The 'facebook_data' directory was not found."
    echo ""
    echo "Please follow these steps:"
    echo "  1. Download your Facebook data from Meta"
    echo "  2. Extract the ZIP file"
    echo "  3. Create a folder: mkdir facebook_data"
    echo "  4. Copy all extracted files into facebook_data/"
    echo ""
    echo "For detailed instructions, see: BREACH_ANALYSIS_GUIDE.md"
    echo ""
    echo "Once you've added your data, run this script again."
    echo ""
    exit 0
fi

echo "✅ Facebook data directory found!"
echo ""

# Run the data checker
echo "📋 STEP 2: Verifying Data Structure"
echo "-----------------------------------------------------------"
echo ""
python3 check_data.py
echo ""

# Ask if user wants to proceed
read -p "Do you want to run the full breach analysis now? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📋 STEP 3: Running Breach Analysis"
    echo "-----------------------------------------------------------"
    echo ""
    python3 analyze_breach.py
    echo ""
    
    echo "==========================================================="
    echo "  Analysis Complete!"
    echo "==========================================================="
    echo ""
    echo "Next steps:"
    echo "  1. Review BREACH_REPORT.md for automated findings"
    echo "  2. Check timeline.txt for chronological events"
    echo "  3. Review suspicious_ips.txt for suspicious IP addresses"
    echo "  4. Fill out INVESTIGATION_TEMPLATE.md with your findings"
    echo "  5. Use INDICATORS_OF_COMPROMISE.md as a checklist"
    echo ""
    echo "For your legal case:"
    echo "  - Compile all evidence in an organized folder"
    echo "  - Cross-reference automated findings with your memories"
    echo "  - Document alibis for suspicious login times/locations"
    echo "  - Consult with legal counsel if needed"
    echo ""
else
    echo ""
    echo "Skipping full analysis. You can run it later with:"
    echo "  python3 analyze_breach.py"
    echo ""
fi

echo "📚 Additional Resources:"
echo "  - BREACH_ANALYSIS_GUIDE.md - Complete guide"
echo "  - INDICATORS_OF_COMPROMISE.md - What to look for"
echo "  - INVESTIGATION_TEMPLATE.md - Document your findings"
echo "  - README.md - Project overview"
echo ""
echo "Good luck with your investigation and legal case!"
echo ""
