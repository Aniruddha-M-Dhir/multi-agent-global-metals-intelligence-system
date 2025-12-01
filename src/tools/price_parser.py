"""
Price Parser Tool
Basic validation and cleaning functions for price data.
"""

def validate_price(value):
    """
    Ensures a price value is valid (positive number).
    """
    if value is None:
        return False
    if not isinstance(value, (int, float)):
        return False
    if value <= 0:
        return False
    return True

def clean_price(value):
    """
    Ensures price is numeric and rounded properly.
    """
    try:
        return round(float(value), 2)
    except:
        return None

