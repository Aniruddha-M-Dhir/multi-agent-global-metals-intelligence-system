"""
Orchestrator Agent
Coordinates the other agents to produce a unified metals intelligence report.
"""

from src.agents.market_data_agent import MarketDataAgent
from src.agents.fx_agent import FXAgent
from src.agents.trend_agent import TrendAgent
from src.agents.arbitrage_agent import ArbitrageAgent

class OrchestratorAgent:
    def __init__(self):
        self.market_agent = MarketDataAgent()
        self.fx_agent = FXAgent()
        self.trend_agent = TrendAgent()
        self.arbitrage_agent = ArbitrageAgent()

    def run_analysis(self, metal: str, target_currency: str):
        # 1. Fetch global market data
        raw_prices = self.market_agent.get_prices(metal)

        # 2. Convert everything to the target currency
        normalized_prices = self.fx_agent.normalize_prices(raw_prices, target_currency)

        # 3. Analyze recent movement (simple simulated trends)
        trend_info = self.trend_agent.analyze_trend(normalized_prices)

        # 4. Detect cross-market differences
        arbitrage_info = self.arbitrage_agent.find_arbitrage(normalized_prices)

        # 5. Return final unified report
        return {
            "metal": metal,
            "target_currency": target_currency,
            "prices": normalized_prices,
            "trend": trend_info,
            "arbitrage": arbitrage_info
        }

# Example manual test
if __name__ == "__main__":
    orch = OrchestratorAgent()
    report = orch.run_analysis("gold", "USD")
    print(report)

