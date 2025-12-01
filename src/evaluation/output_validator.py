"""
Output Validator
Simple evaluation tool to verify that agent outputs
have the correct structure and required fields.
"""

class OutputValidator:

    REQUIRED_FIELDS = ["metal", "target_currency", "prices", "trend", "arbitrage"]

    def validate(self, report: dict):
        """
        Validates the final orchestrator output.
        Ensures all required fields are present and correctly typed.
        """
        missing = [field for field in self.REQUIRED_FIELDS if field not in report]

        if missing:
            return {
                "valid": False,
                "message": f"Missing required fields: {missing}"
            }

        if not isinstance(report["prices"], dict):
            return {
                "valid": False,
                "message": "Prices field must be a dictionary."
            }

        if not isinstance(report["trend"], dict):
            return {
                "valid": False,
                "message": "Trend field must be a dictionary."
            }

        if not isinstance(report["arbitrage"], dict):
            return {
                "valid": False,
                "message": "Arbitrage field must be a dictionary."
            }

        return {
            "valid": True,
            "message": "Output structure is valid."
        }

