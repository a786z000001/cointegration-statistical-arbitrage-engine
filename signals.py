import numpy as np

def generate_signals(df, beta, window):
    df['spread'] = df['stock1'] - beta * df['stock2']

    # rolling stats (this is "adaptive behavior")
    df['mean'] = df['spread'].rolling(window).mean()
    df['std'] = df['spread'].rolling(window).std()

    df['zscore'] = (df['spread'] - df['mean']) / df['std']

    df['signal'] = 0
    df.loc[df['zscore'] < -1, 'signal'] = 1
    df.loc[df['zscore'] > 1, 'signal'] = -1

    return df