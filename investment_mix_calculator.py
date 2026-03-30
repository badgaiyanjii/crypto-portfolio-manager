class InvestmentMixCalculator:

    def __init__(self, risk_metrics, total_investment, risk_profile):

        self.risk_metrics = risk_metrics
        self.total = total_investment
        self.profile = risk_profile

    def calculate_allocation(self):

        allocation = []

        if self.profile == "Low":
            weights = {"LOW":0.6,"MEDIUM":0.3,"HIGH":0.1}

        elif self.profile == "Medium":
            weights = {"LOW":0.3,"MEDIUM":0.4,"HIGH":0.3}

        else:
            weights = {"LOW":0.1,"MEDIUM":0.3,"HIGH":0.6}

        counts = {"LOW":0,"MEDIUM":0,"HIGH":0}

        for coin in self.risk_metrics:
            counts[coin["risk_level"]] += 1

        for coin in self.risk_metrics:

            cat = coin["risk_level"]

            if counts[cat] == 0:
                continue

            amount = (weights[cat] * self.total) / counts[cat]

            allocation.append({

                "coin_id": coin["coin_id"],
                "risk_level": cat,
                "allocated_amount": round(amount,2)

            })

        return allocation