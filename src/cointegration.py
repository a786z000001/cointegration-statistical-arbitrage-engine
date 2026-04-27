from statsmodels.tsa.stattools import coint
import statsmodels.api as sm

def check_cointegration(df):
    score, pvalue, _ = coint(df['stock1'], df['stock2'])
    return pvalue

def compute_hedge_ratio(df):
    X = sm.add_constant(df['stock2'])
    model = sm.OLS(df['stock1'], X).fit()
    #beta = model.params[1]
    beta = model.params['stock2']
    return beta
