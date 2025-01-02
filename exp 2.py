import pandas as pd

def find_positions(series):
    
    positions = []
    
    for i in range(1, len(series) - 1):
        
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            positions.append(i)  
    
    return positions


series = pd.Series([1, 3, 2, 4, 6, 5, 7, 3, 8, 6])


positions = find_positions(series)

print("Positions:", positions)
