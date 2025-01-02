import pandas as pd

def series_to_dataframe(series):

    df = series.reset_index()
    df.columns = ['Index', 'Value']
    
    return df

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

df = series_to_dataframe(series)
print("DataFrame:\n", df)
