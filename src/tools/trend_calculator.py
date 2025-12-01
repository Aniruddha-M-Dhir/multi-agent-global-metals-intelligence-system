"""
Trend Calculator Tool
Utility functions to support trend analysis.
"""

def calculate_range(prices: list):
    """
    Returns the difference between highest and lowest values.
    """
    if not prices:
        return 0
    return round(max(prices) - min(prices), 2)

def trend_signal(range_value):
    """
    Very basic rule-based trend indicator.
    """
    if range_value < 0.5:
        return "Stable"
    elif range_value < 2:
        return "Mild Variation"
    else:
        return "High Variation"

