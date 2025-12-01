"""
Arbitrage Utility Tool
Helper functions to support arbitrage detection.
"""

def calculate_spread(low_price, high_price):
    """
    Returns the absolute price spread.
    """
    return round(high_price - low_price, 2)

def calculate_spread_percent(low_price, high_price):
    """
    Returns the percentage spread between two prices.
    """
    if low_price == 0:
        return 0
    spread = high_price - low_price
    return round((spread / low_price) * 100, 2)

