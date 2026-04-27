import numpy as np

def run_backtest(df, cost):
    # 1. Calculate returns
    df['returns1'] = df['stock1'].pct_change()
    df['returns2'] = df['stock2'].pct_change()

    # 2. Strategy returns (long-short spread)
    df['strategy_returns'] = (
        df['signal'].shift(1) * (df['returns1'] - df['returns2'])
    )

    # 3. Transaction cost (applied on position change)
    df['strategy_returns'] -= cost * abs(df['signal'].diff())

    # 4. Clean NaN values
    df['strategy_returns'] = df['strategy_returns'].fillna(0)

    # 5. Cumulative returns (equity curve)
    df['cum_returns'] = (1 + df['strategy_returns']).cumprod()

    return df
