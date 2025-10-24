"""
Pattern Definitions for IT Ticket Classification
Contains all the regex patterns and mappings used for ticket categorization
"""

# Specific request patterns that indicate automation opportunities
SPECIFIC_PATTERNS = {
    # Financial & Billing
    'Billing and Financial Management': [
        r'billing', r'invoice', r'payment', r'cost', r'expense', r'budget',
        r'migrate.*billing', r'billing.*migration', r'financial.*management',
        r'subscription.*billing', r'vendor.*billing', r'accounting', r'finance'
    ],
    
    # Monitoring & Alerts
    'EverAgCorp247SitePoller Alerts': [
        r'EverAgCorp247SitePoller', r'Site24x7.*Alert.*Mailer'
    ],
    'System Monitoring Alerts': [
        r'monitoring.*alert', r'system.*down', r'service.*unavailable',
        r'server.*down', r'outage.*notification'
    ],
    
    # Security & Access Management
    'Intune Setup and Conditional Access': [
        r'intune.*setup', r'conditional.*access', r'intune.*enroll',
        r'device.*enrollment', r'mdm.*enrollment', r'intune.*configuration'
    ],
    '1Password Setup and Management': [
        r'1password', r'1 password', r'onepassword', r'password.*manager',
        r'1password.*setup', r'1password.*access', r'1password.*vault'
    ],
    'MFA Setup and Issues': [
        r'multi.*factor', r'mfa.*setup', r'two.*factor', r'2fa',
        r'authenticator.*app', r'duo.*setup'
    ],
    'Security Group Management': [
        r'security.*group', r'ad.*group', r'active.*directory.*group',
        r'domain.*group'
    ],
    
    # Email & Communication
    'Email List Management': [
        r'remove.*from.*distribution.*list', r'add.*to.*distribution.*list',
        r'mailing.*list.*change', r'distribution.*group'
    ],
    'Email Forwarding Setup': [
        r'setup.*email.*forwarding', r'forward.*email.*to',
        r'email.*forwarding.*request', r'email.*redirect'
    ],
    'Shared Mailbox Management': [
        r'shared.*mailbox', r'mailbox.*access', r'shared.*email',
        r'mailbox.*permission'
    ],
    'Email Signature Updates': [
        r'email.*signature', r'signature.*update', r'signature.*change',
        r'signature.*setup'
    ],
    'Outlook Configuration': [
        r'outlook.*setup', r'outlook.*configuration', r'outlook.*profile',
        r'email.*client.*setup'
    ],
    
    # Software & Licensing
    'Software License Requests': [
        r'need.*license.*for', r'request.*license', r'software.*license.*needed',
        r'license.*activation'
    ],
    'Software Installation Requests': [
        r'install.*software', r'software.*installation',
        r'need.*software.*installed', r'application.*install'
    ],
    'Office 365 Setup': [
        r'office.*365', r'o365.*setup', r'microsoft.*365', r'm365',
        r'office.*suite'
    ],
    'Adobe License Management': [
        r'adobe.*license', r'creative.*cloud', r'adobe.*access',
        r'photoshop.*license'
    ],
    
    # User Management
    'User Account Deactivation': [
        r'deactivate.*account', r'disable.*account', r'terminate.*user',
        r'offboard.*user', r'remove.*user'
    ],
    'New User Setup': [
        r'new.*user.*setup', r'new.*employee', r'onboard.*user',
        r'create.*account', r'user.*provisioning'
    ],
    'Group Membership Changes': [
        r'add.*to.*group', r'remove.*from.*group', r'group.*membership',
        r'group.*access'
    ],
    'Permission Changes': [
        r'give.*access.*to.*folder', r'permission.*to.*folder',
        r'share.*folder.*with', r'file.*permission'
    ],
    
    # Infrastructure & Network
    'VPN Setup/Configuration': [
        r'setup.*vpn', r'configure.*vpn', r'vpn.*setup', r'vpn.*access',
        r'vpn.*client'
    ],
    'Network Drive Mapping': [
        r'map.*network.*drive', r'connect.*to.*shared.*drive',
        r'shared.*drive.*mapping', r'network.*folder'
    ],
    'Printer Setup': [
        r'setup.*printer', r'install.*printer', r'printer.*installation',
        r'add.*printer', r'printer.*driver'
    ],
    'WiFi Configuration': [
        r'wifi.*setup', r'wireless.*setup', r'wifi.*password',
        r'wireless.*access', r'network.*connection'
    ],
    
    # Hardware & Equipment
    'Equipment Return/Pickup': [
        r'return.*laptop', r'return.*equipment', r'pickup.*laptop',
        r'collect.*equipment', r'asset.*return'
    ],
    'Hardware Requests': [
        r'need.*laptop', r'need.*computer', r'request.*equipment',
        r'hardware.*request', r'new.*workstation'
    ],
    'Monitor Setup': [
        r'monitor.*setup', r'dual.*monitor', r'external.*monitor',
        r'display.*setup', r'screen.*setup'
    ],
    'Phone Setup': [
        r'phone.*setup', r'voip.*setup', r'desk.*phone',
        r'telephone.*setup', r'extension.*setup'
    ],
    
    # System Updates & Maintenance
    'System/Software Updates': [
        r'update.*software', r'software.*update.*needed', r'system.*update',
        r'patch.*update', r'windows.*update'
    ],
    'Backup Requests': [
        r'backup.*request', r'restore.*file', r'file.*recovery',
        r'data.*backup', r'file.*restore'
    ],
    
    # Mobile & Remote Access
    'Mobile Device Setup': [
        r'mobile.*device.*setup', r'iphone.*setup', r'android.*setup',
        r'tablet.*setup', r'phone.*configuration'
    ],
    'Remote Desktop Setup': [
        r'remote.*desktop', r'rdp.*setup', r'remote.*access.*setup',
        r'terminal.*server'
    ],
    
    # Specialized Applications
    'Salesforce Access': [
        r'salesforce.*access', r'salesforce.*setup', r'sfdc',
        r'crm.*access', r'salesforce.*login'
    ],
    'SharePoint Access': [
        r'sharepoint.*access', r'sharepoint.*setup', r'sp.*access',
        r'sharepoint.*permission'
    ],
    'Teams Setup': [
        r'teams.*setup', r'microsoft.*teams', r'teams.*access',
        r'teams.*configuration'
    ],
    'Zoom Configuration': [
        r'zoom.*setup', r'zoom.*access', r'zoom.*configuration',
        r'zoom.*meeting'
    ],
    
    # Administrative Tasks
    'Asset Management': [
        r'asset.*tag', r'inventory.*update', r'asset.*tracking',
        r'equipment.*audit'
    ],
    'Documentation Updates': [
        r'update.*documentation', r'wiki.*update', r'procedure.*update',
        r'knowledge.*base'
    ],
    'Training Requests': [
        r'training.*request', r'user.*training', r'software.*training',
        r'system.*training'
    ]
}

# General IT support patterns
GENERAL_PATTERNS = {
    'Password Reset/Account Lockout': [
        r'password.*reset', r'forgot.*password', r'password.*change',
        r'password.*expire', r'account.*locked', r'locked.*out'
    ],
    'Email/Outlook Issues': [
        r'email.*not.*work', r'outlook.*issue', r'email.*problem',
        r'cannot.*send.*email', r'email.*error', r'outlook.*crash'
    ],
    'Printer/Printing Problems': [
        r'printer.*not.*work', r'cannot.*print', r'printing.*issue',
        r'printer.*jam', r'printer.*offline'
    ],
    'Network/WiFi Connectivity': [
        r'internet.*not.*work', r'wifi.*issue', r'network.*problem',
        r'cannot.*connect', r'connection.*slow'
    ],
    'Hardware Failure/Issues': [
        r'computer.*not.*start', r'laptop.*broken', r'monitor.*not.*work',
        r'hardware.*fail', r'device.*malfunction'
    ],
    'Performance/Speed Issues': [
        r'computer.*slow', r'system.*slow', r'performance.*issue',
        r'running.*slow', r'system.*freeze'
    ],
    'Application Crashes/Errors': [
        r'application.*crash', r'software.*error', r'program.*not.*work',
        r'application.*freeze'
    ],
    'File/Data Issues': [
        r'file.*corrupt', r'data.*loss', r'file.*missing',
        r'cannot.*open.*file', r'file.*error'
    ],
    'Login/Authentication Issues': [
        r'cannot.*login', r'login.*fail', r'authentication.*error',
        r'access.*denied'
    ]
}

# Category mappings for fallback classification
CATEGORY_MAPPINGS = {
    'Applications': 'Specialized Applications',
    'Hardware Setup': 'Hardware & Equipment',
    'Employee Setup': 'User Management',
    'Account Managment': 'User Management',
    'Networking/Server': 'Infrastructure & Network',
    'Infrastructure': 'Infrastructure & Network',
    'Task': 'Administrative Tasks',
    'Alert - Scheduled Outage': 'Monitoring & Alerts',
    'Uncategorized': 'General IT Support',
    'nan': 'General IT Support'
}

# Automation potential scoring
AUTOMATION_SCORING = {
    'HIGH': [
        'Email List Management', 'Email Forwarding Setup', 'VPN Setup/Configuration',
        'Network Drive Mapping', 'Group Membership Changes', 'System/Software Updates'
    ],
    'MEDIUM': [
        'Billing and Financial Management', 'Intune Setup and Conditional Access',
        '1Password Setup and Management', 'Software License Requests',
        'File/Folder Permission Changes', 'User Account Deactivation',
        'EverAgCorp247SitePoller Alerts'
    ],
    'LOW': [
        'Hardware Requests', 'Equipment Return/Pickup', 'Training Requests',
        'Documentation Updates'
    ]
}

def get_automation_score(ticket_type):
    """Get automation potential score for a ticket type"""
    clean_type = ticket_type.replace('🎯 ', '')
    
    for score, types in AUTOMATION_SCORING.items():
        if clean_type in types:
            return score
    
    # Default scoring based on pattern
    if ticket_type.startswith('🎯') and 'Setup' in ticket_type:
        return 'MEDIUM'
    elif ticket_type.startswith('🎯'):
        return 'HIGH'
    else:
        return 'LOW'
