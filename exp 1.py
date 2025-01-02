import pandas as pd
import numpy as np

def euclidean_distance(series1, series2):
    
    array1 = series1.to_numpy()
    array2 = series2.to_numpy()
    
    
    distance = np.linalg.norm(array1 - array2)
    
    return distance


series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])


distance = euclidean_distance(series1, series2)
print(f"Euclidean Distance: {distance}")
