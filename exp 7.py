import pandas as pd

def stack_series(series1, series2):

    vertical_stack = pd.concat([series1, series2], axis=0).reset_index(drop=True)

    horizontal_stack = pd.concat([series1, series2], axis=1)
    
    return vertical_stack, horizontal_stack


data1 = [10, 20, 30]
data2 = [40, 50, 60]
series1 = pd.Series(data1)
series2 = pd.Series(data2)

vertical_stack, horizontal_stack = stack_series(series1, series2)

print("Vertical Stack:\n", vertical_stack)
print("\nHorizontal Stack:\n", horizontal_stack)
