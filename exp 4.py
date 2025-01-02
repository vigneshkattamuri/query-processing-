import pandas as pd

def compute_autocorrelations(series, lag):

    autocorrelation = series.autocorr(lag=lag)
    return autocorrelation


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(data)

lag = 2  
autocorrelation = compute_autocorrelations(series, lag)

print(f"Autocorrelation at lag {lag}: {autocorrelation}")
