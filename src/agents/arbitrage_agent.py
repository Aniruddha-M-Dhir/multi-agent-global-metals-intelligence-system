"""
Arbitrage Agent
Finds pricing gaps between markets after FX normalization.
"""

class ArbitrageAgent:

    def find_arbitrage(self, normalized_prices: dict):
        """
        Finds the cheapest and most expensive markets.
        This simulates arbitrage detection.
        """
        # Extract (market_name, converted_price)
        price_list = [
            (market, info["converted_price"])
            for market, info in normalized_prices.items()
        ]

        # Sort by price
        sorted_prices = sorted(price_list, key=lambda x: x[1])

        cheapest_market, cheap_price = sorted_prices[0]
        expensive_market, high_price = sorted_prices[-1]

        spread = round(high_price - cheap_price, 2)
        spread_percent = round((spread / cheap_price) * 100, 2)

        return {

