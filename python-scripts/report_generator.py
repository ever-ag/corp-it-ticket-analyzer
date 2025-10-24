"""
HTML Report Generator for IT Ticket Analysis
Generates interactive HTML reports with detailed ticket breakdowns
"""

import re
from datetime import datetime
from pattern_definitions import get_automation_score

def generate_html_report(df, detailed_analysis, stats):
    """Generate comprehensive HTML report"""
    
    # Group tickets by type for detailed panels
    tickets_by_type = {}
    for idx, info in detailed_analysis.items():
        ticket_type = info['detected_type']
        if ticket_type not in tickets_by_type:
            tickets_by_type[ticket_type] = []
        tickets_by_type[ticket_type].append(info)
    
    # Sort types by count
    sorted_types = stats['type_counts'].most_common(50)
    sorted_categories = stats['category_counts'].most_common()
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>IT Ticket Analysis Report - {datetime.now().strftime('%Y-%m-%d')}</title>
    <style>
        {get_css_styles()}
    </style>
    <script>
        {get_javascript_functions()}
    </script>
</head>
<body>
    <div class="container">
        <h1>🔍 IT Ticket Analysis Report</h1>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        {generate_summary_section(stats)}
        {generate_category_section(sorted_categories, stats['total_tickets'])}
        {generate_ticket_types_section(sorted_types, stats['total_tickets'], tickets_by_type, detailed_analysis)}
        {generate_insights_section(stats)}
    </div>
</body>
</html>"""
    
    return html_content

def generate_summary_section(stats):
    """Generate executive summary section"""
    return f"""
        <div class="metric">
            <strong>Total Tickets:</strong> {stats['total_tickets']:,} | 
            <strong>Total Time:</strong> {stats['total_time']:.1f} hours | 
            <strong>Average Time:</strong> {stats['average_time']:.1f} hrs/ticket | 
            <strong>🎯 Automation Candidates:</strong> {stats['automation_candidates']:,} tickets
        </div>
        
        <div class="improvement">
            <strong>✅ Analysis Complete:</strong> 
            {stats['unique_types']} unique ticket types identified with 
            {stats['specific_patterns']} specific automation patterns detected
        </div>
    """

def generate_category_section(sorted_categories, total_tickets):
    """Generate category breakdown section"""
    html = """
        <h2>📊 Category Summary</h2>
        <table style="width: 70%;">
            <tr><th>Category</th><th>Count</th><th>%</th><th>Focus Area</th></tr>
    """
    
    for category, count in sorted_categories:
        percentage = (count / total_tickets * 100)
        focus = get_focus_area(category, percentage)
        html += f"<tr><td>{category}</td><td>{count:,}</td><td>{percentage:.1f}%</td><td>{focus}</td></tr>"
    
    html += "</table>"
    return html

def generate_ticket_types_section(sorted_types, total_tickets, tickets_by_type, detailed_analysis):
    """Generate detailed ticket types section"""
    html = """
        <h2>📊 All Ticket Types - Click for Deep Dive Details</h2>
        <table>
            <tr><th>Rank</th><th>Ticket Type</th><th>Category</th><th>Count</th><th>%</th><th>Automation</th></tr>
    """
    
    category_styles = get_category_styles()
    
    for rank, (ticket_type, count) in enumerate(sorted_types, 1):
        percentage = (count / total_tickets * 100)
        safe_id = re.sub(r'[^a-zA-Z0-9]', '', ticket_type)
        
        # Get category for styling
        sample_ticket = next((info for info in detailed_analysis.values() 
                            if info['detected_type'] == ticket_type), None)
        ticket_category = sample_ticket['type_category'] if sample_ticket else 'General IT Support'
        
        automation = get_automation_score(ticket_type)
        row_class = category_styles.get(ticket_category, 'general')
        
        html += f"""
            <tr class="{row_class}">
                <td>{rank}</td>
                <td class="clickable" onclick="toggleDetails('{ticket_type}')">{ticket_type}</td>
                <td>{ticket_category}</td>
                <td>{count:,}</td>
                <td>{percentage:.1f}%</td>
                <td><span class="automation-tag automation-{automation.lower()}">{automation}</span></td>
            </tr>
        """
        
        # Add detail panel for top 30 types
        if rank <= 30:
            html += generate_detail_panel(ticket_type, count, percentage, 
                                        tickets_by_type.get(ticket_type, []), safe_id)
    
    html += "</table>"
    return html

def generate_detail_panel(ticket_type, count, percentage, tickets, safe_id):
    """Generate expandable detail panel for a ticket type"""
    html = f"""
        <tr>
            <td colspan="6">
                <div id="details-{safe_id}" class="detail-panel">
                    <button class="close-btn" onclick="closeDetails('{ticket_type}')">✕</button>
                    <h4>{ticket_type} - {count:,} tickets ({percentage:.1f}%)</h4>
    """
    
    # Show sample tickets
    sample_tickets = sorted(tickets, key=lambda x: x['time_spent'], reverse=True)[:10]
    
    for i, ticket in enumerate(sample_tickets, 1):
        desc_preview = ticket['description'][:200]
        if len(ticket['description']) > 200:
            desc_preview += '...'
        
        html += f"""
            <div class="ticket-item">
                <strong>#{i} - {ticket['ticket_number']}</strong> | 
                <strong>{ticket['time_spent']:.1f}hrs</strong> | 
                <strong>{ticket['status']}</strong> | 
                <strong>{ticket['assigned_to']}</strong><br>
                <strong>Subject:</strong> {ticket['subject']}<br>
                <strong>Description:</strong> {desc_preview}
            </div>
        """
    
    html += "</div></td></tr>"
    return html

def generate_insights_section(stats):
    """Generate insights and recommendations section"""
    automation_percentage = (stats['automation_candidates'] / stats['total_tickets'] * 100)
    
    return f"""
        <div class="metric">
            <h3>🎯 Key Insights & Recommendations</h3>
            <ul>
                <li><strong>Automation Opportunity:</strong> {stats['automation_candidates']:,} tickets ({automation_percentage:.1f}%) are automation candidates</li>
                <li><strong>Process Improvement:</strong> Focus on HIGH automation items for maximum ROI</li>
                <li><strong>Self-Service Potential:</strong> Email management, VPN setup, and software requests</li>
                <li><strong>Knowledge Base Priority:</strong> Create articles for top ticket types</li>
                <li><strong>Resource Planning:</strong> Use time data for better technician allocation</li>
            </ul>
            
            <h3>🚀 Next Steps</h3>
            <ol>
                <li><strong>Implement Self-Service:</strong> Start with email list management and VPN setup</li>
                <li><strong>Automate Workflows:</strong> Create approval processes for access requests</li>
                <li><strong>Create Knowledge Base:</strong> Document solutions for common issues</li>
                <li><strong>Monitor Progress:</strong> Re-run analysis monthly to track improvements</li>
            </ol>
        </div>
    """

def get_focus_area(category, percentage):
    """Determine focus area based on category and percentage"""
    if percentage > 15:
        return "🔥 High Priority"
    elif percentage > 8:
        return "⚡ Medium Priority"
    elif category in ["Security & Access", "Financial & Billing"]:
        return "🎯 Strategic Focus"
    else:
        return "📋 Standard Process"

def get_category_styles():
    """Return CSS class mappings for categories"""
    return {
        'Monitoring & Alerts': 'monitoring',
        'Security & Access': 'security',
        'Email & Communication': 'email',
        'Software & Licensing': 'software',
        'User Management': 'user-mgmt',
        'Infrastructure & Network': 'infrastructure',
        'Hardware & Equipment': 'hardware',
        'System Maintenance': 'maintenance',
        'Mobile & Remote': 'mobile',
        'Specialized Applications': 'specialized',
        'General IT Support': 'general',
        'Administrative Tasks': 'admin',
        'Financial & Billing': 'billing'
    }

def get_css_styles():
    """Return CSS styles for the report"""
    return """
        body { font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }
        .container { max-width: 1800px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 8px; }
        h1 { color: #2c3e50; text-align: center; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; border-left: 4px solid #3498db; padding-left: 15px; }
        table { width: 100%; border-collapse: collapse; margin: 15px 0; font-size: 10px; }
        th, td { border: 1px solid #bdc3c7; padding: 4px; text-align: left; }
        th { background-color: #3498db; color: white; }
        tr:nth-child(even) { background-color: #f8f9fa; }
        .clickable { color: #3498db; cursor: pointer; text-decoration: underline; font-weight: bold; }
        .clickable:hover { background-color: #e8f4fd; }
        .monitoring { background-color: #e8f5e8; }
        .security { background-color: #f0e6ff; }
        .email { background-color: #e6f3ff; }
        .software { background-color: #fff0e6; }
        .user-mgmt { background-color: #f0fff0; }
        .infrastructure { background-color: #ffe6e6; }
        .hardware { background-color: #fff3e0; }
        .maintenance { background-color: #f5f5f5; }
        .mobile { background-color: #e8f4f8; }
        .specialized { background-color: #ffeef8; }
        .general { background-color: #f8f8f8; }
        .admin { background-color: #f0f8ff; }
        .billing { background-color: #fff9e6; }
        .detail-panel { display: none; background-color: #f8f9fa; padding: 10px; margin: 2px 0; border-radius: 5px; border: 1px solid #bdc3c7; }
        .ticket-item { background-color: white; margin: 2px 0; padding: 6px; border-radius: 3px; border-left: 3px solid #3498db; font-size: 9px; }
        .close-btn { float: right; background: #e74c3c; color: white; border: none; padding: 2px 6px; border-radius: 3px; cursor: pointer; }
        .metric { background-color: #e8f4fd; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .improvement { background-color: #d4edda; padding: 10px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #28a745; }
        .automation-tag { color: white; padding: 1px 4px; border-radius: 3px; font-size: 8px; }
        .automation-high { background-color: #27ae60; }
        .automation-medium { background-color: #f39c12; }
        .automation-low { background-color: #95a5a6; }
    """

def get_javascript_functions():
    """Return JavaScript functions for interactivity"""
    return """
        function toggleDetails(ticketType) {
            var panel = document.getElementById('details-' + ticketType.replace(/[^a-zA-Z0-9]/g, ''));
            if (panel.style.display === 'none' || panel.style.display === '') {
                panel.style.display = 'block';
            } else {
                panel.style.display = 'none';
            }
        }
        
        function closeDetails(ticketType) {
            var panel = document.getElementById('details-' + ticketType.replace(/[^a-zA-Z0-9]/g, ''));
            panel.style.display = 'none';
        }
    """
