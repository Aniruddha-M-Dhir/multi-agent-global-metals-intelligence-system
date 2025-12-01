Multi-Agent Global Precious Metals Intelligence System
A multi-agent system that analyzes global precious metals prices (gold, silver, platinum) across multiple markets, normalizes them into any currency, detects trends, and highlights arbitrage-like opportunities. Built as a Capstone Project for the Google × Kaggle Agents Intensive.

🏆 Overview
Global precious metals prices vary between exchanges like New York, London, Shanghai, Dubai, and Mumbai. Each market uses different currencies and spreads, making comparisons difficult.
This project demonstrates how an agentic system can:
fetch simulated prices from global markets
convert them into a single target currency
analyze short-term price variation
detect cross-market spreads
produce a unified intelligence report
It uses a clean, well-documented multi-agent architecture suitable for explanation and evaluation.

🧠 Architecture
This project uses five cooperating agents plus a memory and evaluation system:
1. Orchestrator Agent
Coordinates all other agents and assembles the final report.
2. Market Data Agent
Simulates fetching prices for gold, silver, and platinum from major global markets.
3. FX Agent
Converts all market prices into the user’s preferred currency (USD, GBP, CNY, AED, INR).
4. Trend Agent
Analyzes price ranges to generate a simple trend direction.
5. Arbitrage Agent
Identifies pricing gaps between markets and calculates the spread.
Memory Manager
Stores basic preferences (preferred metal and currency).
Evaluation Tool
Validates structure and consistency of the final orchestrator output.

📁 Project Structure
src/
  orchestrator/
    orchestrator_agent.py
  agents/
    market_data_agent.py
    fx_agent.py
    trend_agent.py
    arbitrage_agent.py
  tools/
    fx_converter.py
    price_parser.py
    trend_calculator.py
    arbitrage_utils.py
  memory/
    memory_manager.py
    user_preferences.json
  evaluation/
    output_validator.py

▶️ How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run the orchestrator
python src/orchestrator/orchestrator_agent.py
3. Example output
The orchestrator prints a JSON-like intelligence report:
{
  "metal": "gold",
  "target_currency": "USD",
  "prices": {...},
  "trend": {...},
  "arbitrage": {...}
}


📊 What This Project Demonstrates
This repository is designed for educational clarity rather than live data accuracy. It demonstrates:
multi-agent orchestration
simulated parallel data flows
tool-based operations
currency normalization logic
trend and arbitrage analysis
memory/state management
evaluation and validation
🧩 Extensions (Planned)
If more time were available, future improvements could include:
real API-based market prices
web dashboard visualization
historical trend lines
predictive modeling
deployment on Cloud Run
real-time alerts and notifications
📜 License
Open source; free to use for learning and experimentation.
