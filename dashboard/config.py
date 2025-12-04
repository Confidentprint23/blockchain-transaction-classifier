# config.py

# App Configuration
APP_TITLE = "Blockchain Transaction Analyzer"
APP_ICON = "🔗"

# Model Thresholds
ANOMALY_THRESHOLD = 0.1
RISK_THRESHOLDS = {
    'low': (0, 0.3),
    'medium': (0.3, 0.6),
    'high': (0.6, 0.8),
    'critical': (0.8, 1.0)
}

# Colors
COLOR_SCHEME = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'success': 'green',
    'warning': 'orange',
    'danger': 'red'
}