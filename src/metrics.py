import numpy as np

def calculate_metrics(df):
    returns = df['strategy_returns'].dropna()

    sharpe = (returns.mean() / returns.std()) * np.sqrt(252)

    drawdown = (df['cum_returns'] / df['cum_returns'].cummax() - 1).min()

    return sharpe, drawdown
