from config import *
from src.data_loader import load_data
from src.cointegration import check_cointegration, compute_hedge_ratio
from src.signals import generate_signals
from src.backtest import run_backtest
from src.metrics import calculate_metrics

import matplotlib.pyplot as plt

def main():
    # 1. Load data
    df = load_data(STOCK1, STOCK2, START_DATE)

    # 2. Cointegration test
    pvalue = check_cointegration(df)
    print("Cointegration p-value:", pvalue)
    print("Cointegrated:", pvalue < 0.05)

    # 3. Hedge ratio
    beta = compute_hedge_ratio(df)
    print("Hedge Ratio (beta):", beta)

    # 4. Signals
    df = generate_signals(df, beta, WINDOW)

    # 5. Backtest
    df = run_backtest(df, TRANSACTION_COST)

    # 6. Metrics
    sharpe, drawdown = calculate_metrics(df)
    print("Total Return:", df['cum_returns'].iloc[-1])
    print("Sharpe Ratio:", sharpe)
    print("Max Drawdown:", drawdown)

    # 7. Plot
    plt.figure(figsize=(10,5))
    plt.plot(df['cum_returns'], label="Strategy")
    plt.legend()
    plt.title("Pair Trading Performance")
    plt.show()

if __name__ == "__main__":
    main()