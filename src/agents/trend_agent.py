"""
Trend Analysis Agent
Provides a simple trend estimation based on normalized prices.
This is lightweight but demonstrates analytical capability.
"""

class TrendAgent:

    def analyze_trend(self, normalized_prices: dict):
        """
        Creates a basic trend summary by comparing the highest
        and lowest normalized market prices.
        """
        converted_values = [
            info["converted_price"]
            for info in normalized_prices.values()
        ]

        high = max(converted_values)
        low = min(converted_values)

        # Simple directional signal
        if high - low < 0.5:
            signal = "Stable"
        elif high > low:
            signal = "Mixed / Slight Upward Pressure"
        else:
            signal = "Unclear"

        return {
            "highest_price": high,
            "lowest_price": low,
            "price_range": round(high - low, 2),
            "trend_signal": signal
        }

