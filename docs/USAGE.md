# 📖 Usage Guide

## Quick Start Options

### 🌐 Option 1: Web-Based Analyzer (Recommended)

The easiest way to analyze your tickets:

1. **Open the Web Analyzer**
   ```bash
   # Navigate to the web-analyzer directory
   cd web-analyzer
   # Open ticket_analyzer.html in your browser
   open ticket_analyzer.html  # macOS
   # or double-click the file
   ```

2. **Upload Your Excel File**
   - Drag and drop your Excel file onto the upload area
   - Or click to browse and select your file
   - Supported formats: `.xlsx`, `.xls`

3. **Wait for Analysis**
   - Progress bar shows analysis status
   - Processing typically takes 10-30 seconds

4. **Review Results**
   - Interactive results display in the browser
   - Click ticket types to see sample tickets
   - Download complete HTML report

### 🐍 Option 2: Python Script Analysis

For command-line usage or automation:

1. **Install Dependencies**
   ```bash
   pip install pandas openpyxl
   ```

2. **Run Analysis**
   ```bash
   cd python-scripts
   python comprehensive_analysis.py your_tickets.xlsx
   ```

3. **Output**
   - Generates timestamped HTML report
   - Console summary of key findings
   - Interactive report with clickable details

## 📋 Excel File Requirements

### Required Columns
Your Excel file should contain these columns (exact names may vary):

| Column | Purpose | Examples |
|--------|---------|----------|
| **Description/Subject** | Ticket content | "Description, Description Additional Details, Additional Notes" |
| **Category** | Original categorization | "Applications", "Hardware Setup", "Infrastructure" |
| **Total Time Spent (Hours)** | Time investment | 1.5, 2.0, 0.25 |
| **Status** | Current status | "Closed", "Open", "In Progress" |
| **Assigned To** | Technician | "John Smith", "IT Team" |
| **Help Ticket Number** | Unique ID | "IT-2025-001", "CORP-12345" |
| **Created By** | Requester | "jane.doe@company.com" |

### Column Name Flexibility
The analyzer automatically detects columns with similar names:
- **Description**: "Description", "Details", "Notes", "Summary"
- **Time**: "Hours", "Time Spent", "Duration", "Time"
- **Category**: "Category", "Type", "Classification"
- **Status**: "Status", "State", "Condition"

### Sample Data Format
```
| Description | Category | Total Time Spent (Hours) | Status | Assigned To |
|-------------|----------|---------------------------|---------|-------------|
| User needs access to SharePoint site | Applications | 0.5 | Closed | John Smith |
| Setup VPN for remote worker | Infrastructure | 1.0 | Closed | Jane Doe |
| Install Office 365 on new laptop | Software | 0.75 | Open | IT Team |
```

## 🎯 Understanding the Output

### Report Sections

1. **Executive Summary**
   - Total tickets and time investment
   - Automation candidates identified
   - Key performance metrics

2. **Category Breakdown**
   - High-level categorization
   - Focus area recommendations
   - Resource allocation insights

3. **Detailed Ticket Types**
   - Specific patterns identified
   - Automation potential scoring
   - Sample ticket examples

4. **Insights & Recommendations**
   - Actionable improvement suggestions
   - Implementation roadmap
   - ROI opportunities

### Color Coding System

| Color | Category | Focus |
|-------|----------|-------|
| 🟢 Green | Monitoring & Alerts | System health |
| 🟣 Purple | Security & Access | Security tools |
| 🔵 Blue | Email & Communication | Communication tools |
| 🟠 Orange | Software & Licensing | Software management |
| 🟢 Light Green | User Management | Account management |
| 🔴 Light Red | Infrastructure & Network | Network services |
| 🟡 Yellow | Financial & Billing | Financial processes |

### Automation Scoring

- **🟢 HIGH**: Self-service potential, immediate ROI
- **🟡 MEDIUM**: Workflow automation, moderate effort
- **⚪ LOW**: Manual processes, limited automation

## 🔧 Customization Options

### Adding New Patterns

Edit `python-scripts/pattern_definitions.py`:

```python
SPECIFIC_PATTERNS = {
    'Your Custom Pattern': [
        r'keyword1.*pattern',
        r'another.*regex.*pattern',
        r'case.*insensitive.*match'
    ]
}
```

### Custom Categories

Modify category mappings:

```python
CATEGORY_MAPPINGS = {
    'Your Category': 'Mapped Category',
    'Custom Type': 'General IT Support'
}
```

### Automation Scoring

Adjust automation potential:

```python
AUTOMATION_SCORING = {
    'HIGH': ['Your High Priority Pattern'],
    'MEDIUM': ['Medium Priority Pattern'],
    'LOW': ['Low Priority Pattern']
}
```

## 🚨 Troubleshooting

### Common Issues

**File Upload Fails**
- Ensure file is .xlsx or .xls format
- Check file isn't corrupted or password protected
- Try saving Excel file in compatibility mode

**Missing Columns**
- Analyzer will use available columns
- Check column names match expected patterns
- Manually map columns if needed

**No Patterns Detected**
- Review pattern definitions
- Check if descriptions contain expected keywords
- Consider adding custom patterns

**Performance Issues**
- Large files (>10,000 tickets) may take longer
- Close other browser tabs for web analyzer
- Use Python script for very large datasets

### Getting Help

1. **Check Examples**: Review `examples/` folder
2. **Read Documentation**: See `docs/` folder
3. **GitHub Issues**: Report bugs or request features
4. **Sample Data**: Use provided sample format

## 📊 Best Practices

### Data Preparation
- Clean up ticket descriptions before analysis
- Standardize category names
- Ensure time data is numeric
- Remove test or duplicate tickets

### Analysis Frequency
- **Monthly**: Track improvement trends
- **Quarterly**: Major process reviews
- **After Changes**: Measure impact of improvements

### Action Planning
1. **Start Small**: Focus on HIGH automation items
2. **Measure Impact**: Track ticket volume changes
3. **Iterate**: Refine patterns based on results
4. **Scale Up**: Expand to MEDIUM automation items

### Sharing Results
- Export HTML reports for stakeholders
- Use insights for budget planning
- Share automation recommendations with management
- Track ROI of implemented improvements
