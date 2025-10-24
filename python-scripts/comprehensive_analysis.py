#!/usr/bin/env python3
"""
IT Ticket Analyzer - Comprehensive Analysis Script
Analyzes IT help desk tickets and generates detailed HTML reports
"""

import pandas as pd
import re
import sys
from collections import Counter
from datetime import datetime
from pattern_definitions import SPECIFIC_PATTERNS, GENERAL_PATTERNS, CATEGORY_MAPPINGS
from report_generator import generate_html_report

def analyze_tickets(file_path):
    """Main analysis function"""
    try:
        # Load Excel file
        df = pd.read_excel(file_path)
        print(f"📊 Loaded {len(df):,} tickets from {file_path}")
        
        # Combine description fields
        df['full_description'] = (
            df.get('Description, Description Additional Details, Additional Notes', '').fillna('') + 
            ' ' + df.get('Subject', '').fillna('')
        )
        
        # Classify tickets
        df, detailed_analysis = classify_tickets(df)
        
        # Generate statistics
        stats = generate_statistics(df, detailed_analysis)
        
        # Generate HTML report
        output_file = f"ticket_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        html_content = generate_html_report(df, detailed_analysis, stats)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Analysis complete! Report saved to: {output_file}")
        print_summary(stats)
        
        return output_file
        
    except Exception as e:
        print(f"❌ Error analyzing tickets: {e}")
        return None

def classify_tickets(df):
    """Classify tickets using pattern matching"""
    ticket_types = []
    ticket_categories = []
    detailed_analysis = {}
    
    for idx, row in df.iterrows():
        text = str(row['full_description'])
        text_lower = text.lower()
        category = str(row.get('Category', ''))
        
        # Find matching pattern
        matched_type, matched_category = find_pattern_match(text_lower, category)
        
        ticket_types.append(matched_type)
        ticket_categories.append(matched_category)
        
        # Store detailed info
        detailed_analysis[idx] = {
            'category': category,
            'detected_type': matched_type,
            'type_category': matched_category,
            'subject': row.get('Subject', ''),
            'description': text,
            'time_spent': pd.to_numeric(row.get('Total Time Spent (Hours)', 0), errors='coerce') or 0,
            'assigned_to': row.get('Assigned To', ''),
            'status': row.get('Status', ''),
            'ticket_number': row.get('Help Ticket Number', ''),
            'created_by': row.get('Created By', '')
        }
    
    df['detected_ticket_type'] = ticket_types
    df['ticket_category'] = ticket_categories
    
    return df, detailed_analysis

def find_pattern_match(text, category):
    """Find the best pattern match for a ticket"""
    
    # Check specific patterns first
    for ticket_type, patterns in SPECIFIC_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return f"🎯 {ticket_type}", get_category_for_type(ticket_type)
    
    # Check general patterns
    for ticket_type, patterns in GENERAL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                return ticket_type, "General IT Support"
    
    # Fallback using category
    mapped_category = CATEGORY_MAPPINGS.get(category, "General IT Support")
    
    # Create contextual type based on keywords
    if any(term in text for term in ['setup', 'configure', 'install']):
        return f"Setup/Configuration - {category}", mapped_category
    elif any(term in text for term in ['access', 'permission', 'login']):
        return f"Access Request - {category}", mapped_category
    elif any(term in text for term in ['issue', 'problem', 'error', 'not work']):
        return f"Technical Issue - {category}", mapped_category
    elif any(term in text for term in ['request', 'need', 'want']):
        return f"Service Request - {category}", mapped_category
    else:
        return f"Other - {category}", mapped_category

def get_category_for_type(ticket_type):
    """Map ticket type to category"""
    if any(x in ticket_type for x in ['Billing', 'Financial']):
        return "Financial & Billing"
    elif any(x in ticket_type for x in ['Intune', 'MFA', '1Password', 'Security']):
        return "Security & Access"
    elif any(x in ticket_type for x in ['Email', 'Mailbox', 'Signature']):
        return "Email & Communication"
    elif any(x in ticket_type for x in ['License', 'Software', 'Office', 'Adobe']):
        return "Software & Licensing"
    elif any(x in ticket_type for x in ['User', 'Account', 'Group', 'Permission']):
        return "User Management"
    elif any(x in ticket_type for x in ['VPN', 'Network', 'Printer', 'WiFi']):
        return "Infrastructure & Network"
    elif any(x in ticket_type for x in ['Equipment', 'Hardware', 'Monitor', 'Phone']):
        return "Hardware & Equipment"
    elif any(x in ticket_type for x in ['Update', 'Backup', 'Disk']):
        return "System Maintenance"
    elif any(x in ticket_type for x in ['Mobile', 'Remote']):
        return "Mobile & Remote"
    elif any(x in ticket_type for x in ['EverAgCorp247SitePoller', 'Monitoring']):
        return "Monitoring & Alerts"
    elif any(x in ticket_type for x in ['Asset', 'Documentation', 'Training']):
        return "Administrative Tasks"
    else:
        return "Specialized Applications"

def generate_statistics(df, detailed_analysis):
    """Generate analysis statistics"""
    type_counts = Counter(df['detected_ticket_type'])
    category_counts = Counter(df['ticket_category'])
    
    df['time_numeric'] = pd.to_numeric(df.get('Total Time Spent (Hours)', 0), errors='coerce').fillna(0)
    total_time = df['time_numeric'].sum()
    
    specific_types = [t for t in type_counts.keys() if t.startswith('🎯')]
    
    return {
        'total_tickets': len(df),
        'total_time': total_time,
        'average_time': total_time / len(df) if len(df) > 0 else 0,
        'unique_types': len(type_counts),
        'specific_patterns': len(specific_types),
        'type_counts': type_counts,
        'category_counts': category_counts,
        'automation_candidates': sum(type_counts[t] for t in specific_types)
    }

def print_summary(stats):
    """Print analysis summary to console"""
    print(f"\n📈 Analysis Summary:")
    print(f"   • Total Tickets: {stats['total_tickets']:,}")
    print(f"   • Total Time: {stats['total_time']:.1f} hours")
    print(f"   • Average Time: {stats['average_time']:.1f} hours/ticket")
    print(f"   • Unique Types: {stats['unique_types']}")
    print(f"   • Specific Patterns: {stats['specific_patterns']}")
    print(f"   • Automation Candidates: {stats['automation_candidates']:,} tickets")
    
    print(f"\n🎯 Top Categories:")
    for category, count in stats['category_counts'].most_common(5):
        percentage = (count / stats['total_tickets'] * 100)
        print(f"   • {category}: {count:,} tickets ({percentage:.1f}%)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python comprehensive_analysis.py <excel_file>")
        print("Example: python comprehensive_analysis.py tickets.xlsx")
        sys.exit(1)
    
    file_path = sys.argv[1]
    analyze_tickets(file_path)
