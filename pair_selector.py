pairs = [
    ("RELIANCE.NS", "ONGC.NS"),
    ("TCS.NS", "INFY.NS"),
    ("HDFCBANK.NS", "ICICIBANK.NS"),
]

def find_best_pair(results):
    return sorted(results, key=lambda x: x['sharpe'], reverse=True)