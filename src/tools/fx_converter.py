"""
FX Converter Tool
Simple helper functions used by the FX Agent.
"""

def convert_currency(amount: float, source_rate: float, target_rate: float) -> float:
    """
    Convert between currencies using rate → USD → target conversion.
    """
    usd_value = amount * source_rate
    return round(usd_value / target_rate, 2)

