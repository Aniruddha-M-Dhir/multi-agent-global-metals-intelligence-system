"""
FX Agent
Normalizes market prices into a single target currency.
Uses simple simulated FX conversion rates for demonstration.
"""

class FXAgent:

    def __init__(self):
        # Simple simulated FX rates relative to USD
        self.fx_rates = {
            "USD": 1.0,
            "GBP": 1.25,
            "CNY": 0.14,
            "AED": 0.27,
            "INR": 0.012
        }

    def normalize_prices(self, price_data: dict, target_currency: str):
        """
        Converts all market prices into the user's target currency.
        """
        target_rate = self.fx_rates.get(target_currency.upper(), 1.0)

        normalized = {}

        for market, info in price_data.items():
            local_currency = info["currency"]
            local_price = info["price"]

            local_rate = self.fx_rates.get(local_currency, 1.0)

            # Convert to USD first → then to target currency
            usd_value = local_price * local_rate
            target_value = round(usd_value / target_rate, 2)

            normalized[market] = {
                "original_price": local_price,
                "original_currency": local_currency,
                "converted_price": target_value,
                "target_currency": target_currency.upper()
            }

        return normalized
