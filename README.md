# 🎯 Corp IT Ticket Analyzer

**Automated IT Help Desk Ticket Analysis & Categorization Tool**

Transform your IT support ticket data into actionable insights with automated pattern recognition, intelligent categorization, and comprehensive reporting.

## 🚀 Features

### 📊 **Intelligent Ticket Classification**
- **40+ Specific Pattern Recognition** - Automatically identifies common IT request types
- **Smart Categorization** - Groups tickets into 12 major categories with color coding
- **Automation Scoring** - Identifies HIGH/MEDIUM/LOW automation potential for each ticket type

### 🎯 **Specific Request Types Detected**
- **Billing & Financial Management** - Invoice processing, cost management, vendor billing
- **Security & Access Management** - 1Password, MFA, Intune, Conditional Access
- **Email & Communication** - Distribution lists, forwarding, shared mailboxes
- **User Management** - New user setup, account deactivation, group membership
- **Infrastructure & Network** - VPN setup, network drives, printer configuration
- **Software & Licensing** - License requests, software installation, Office 365
- **Hardware & Equipment** - Equipment requests, returns, monitor setup
- **Monitoring & Alerts** - System monitoring, EverAgCorp247SitePoller alerts
- **And many more...**

### 📈 **Comprehensive Analytics**
- **Volume Analysis** - Ticket counts and percentages by type
- **Time Investment** - Total and average time spent per category
- **Trend Identification** - Spot patterns for process improvement
- **Interactive Deep Dive** - Click any ticket type to see sample tickets

### 🌐 **Multiple Analysis Options**
1. **Web-Based Analyzer** - Upload Excel files directly in browser
2. **Python Scripts** - Command-line analysis for automation
3. **Interactive HTML Reports** - Clickable, detailed analysis reports

## 📁 Repository Structure

```
corp-it-ticket-analyzer/
├── web-analyzer/
│   └── ticket_analyzer.html          # Web-based upload & analysis tool
├── python-scripts/
│   ├── comprehensive_analysis.py     # Main analysis script
│   ├── pattern_definitions.py        # Ticket pattern configurations
│   └── report_generator.py          # HTML report generation
├── examples/
│   ├── sample_analysis_report.html   # Example output report
│   └── sample_data_format.xlsx      # Expected Excel format
├── docs/
│   ├── USAGE.md                     # Detailed usage instructions
│   ├── PATTERNS.md                  # Complete pattern documentation
│   └── CUSTOMIZATION.md             # How to add new patterns
└── README.md                        # This file
```

## 🏃‍♂️ Quick Start

### Option 1: Web-Based Analysis (Easiest)
1. Open `web-analyzer/ticket_analyzer.html` in your browser
2. Upload your Excel file (drag & drop or click)
3. Wait for analysis to complete
4. Download the generated HTML report

### Option 2: Python Script Analysis
```bash
# Clone the repository
git clone https://github.com/ever-ag/corp-it-ticket-analyzer.git
cd corp-it-ticket-analyzer

# Run analysis on your Excel file
python python-scripts/comprehensive_analysis.py your_tickets.xlsx

# Output: detailed_ticket_analysis.html
```

## 📋 Excel File Requirements

Your Excel file should contain these columns (names can vary):
- **Description/Subject** - Ticket description and subject
- **Category** - Original ticket category
- **Total Time Spent (Hours)** - Time investment data
- **Status** - Ticket status (Open, Closed, etc.)
- **Assigned To** - Technician assignment
- **Help Ticket Number** - Unique ticket identifier
- **Created By** - Ticket requester

## 🎯 Key Business Value

### **Automation Opportunities Identified**
- **Email List Management** - Self-service portal potential
- **VPN Setup** - Automated provisioning workflows  
- **Software Licensing** - Automated catalog requests
- **1Password Management** - Standardized onboarding
- **New User Setup** - Streamlined provisioning process

### **Process Improvement Insights**
- **High-Volume Categories** - Focus areas for optimization
- **Time Investment Analysis** - Resource allocation insights
- **Pattern Recognition** - Identify training opportunities
- **Knowledge Base Priorities** - Data-driven article creation

### **Real Results Example**
From a 4,377 ticket analysis:
- **1,500+ tickets (34%)** identified as automation candidates
- **15 specific request types** with HIGH automation potential
- **Zero uncategorized tickets** with improved classification
- **Clear ROI path** for self-service implementations

## 🔧 Customization

### Adding New Patterns
Edit `python-scripts/pattern_definitions.py`:
```python
specific_patterns = {
    'Your New Pattern': [
        r'keyword1.*pattern',
        r'another.*pattern',
        r'regex.*pattern'
    ]
}
```

### Custom Categories
Modify category mappings in the classification logic to match your organization's structure.

## 📊 Sample Output

The analyzer generates interactive HTML reports with:
- **Executive Summary** - Key metrics and totals
- **Category Breakdown** - Visual distribution of ticket types
- **Clickable Ticket Types** - Deep dive into specific patterns
- **Sample Tickets** - Real examples for each category
- **Automation Recommendations** - Actionable improvement suggestions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-pattern`)
3. Add your patterns or improvements
4. Test with sample data
5. Submit a pull request

## 📄 License

MIT License - See LICENSE file for details

## 🆘 Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check the `docs/` folder for detailed guides
- **Examples**: See `examples/` for sample data and reports

## 🏷️ Tags

`it-helpdesk` `ticket-analysis` `automation` `data-analysis` `python` `javascript` `excel` `reporting` `process-improvement` `self-service`

---

**Transform your IT support data into actionable insights today!** 🚀
