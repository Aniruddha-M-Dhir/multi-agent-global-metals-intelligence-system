"""
Market Data Agent
Simulates fetching metal prices from global markets.
This keeps things simple but realistic for the Capstone project.
"""

class MarketDataAgent:

    def __init__(self):
        # Simulated markets and currencies (example values)
        self.markets = {
            "New York": "USD",
            "London": "GBP",
            "Shanghai": "CNY",
            "Dubai": "AED",
            "Mumbai": "INR"
        }

    def get_prices(self, metal: str):
        """
        Simulated price fetch.
        In a real system, these would come from APIs or tools.
        """
        # For demonstration, return fixed simulated values
        base_prices = {
            "gold": 100,
            "silver": 1.2,
            "platinum": 30
        }

        base = base_prices.get(metal.lower(), 100)

        # Simulated random-ish spreads per market
        prices = {
            market: round(base * (1 + i * 0.01), 2)
            for i, market in enumerate(self.markets.keys())
        }

        # Attach currency for each market
        result = {
            market: {
                "price": price,
                "currency": self.markets[market]
            }
            for market, price in prices.items()
        }

        return result

