def calculate_credit_score(data):

    character = data["litigation_score"] * 0.2
    capacity = data["cashflow_score"] * 0.3
    capital = data["networth_score"] * 0.2
    collateral = data["asset_score"] * 0.2
    conditions = data["sector_score"] * 0.1

    score = character + capacity + capital + collateral + conditions

    return round(score,2)
