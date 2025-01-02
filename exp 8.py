import numpy as np

def pearson_correlation(x, y):
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    
    diff_x = x - mean_x
    diff_y = y - mean_y

    product = np.sum(diff_x * diff_y)
  
    sum_sq_x = np.sum(diff_x ** 2)
    sum_sq_y = np.sum(diff_y ** 2)
    
   
    r_xy = product / np.sqrt(sum_sq_x * sum_sq_y)
    
    return r_xy


x = np.array([6, 8, 10])
y = np.array([12, 10, 20])


r_xy = pearson_correlation(x, y)
print(f"Pearson's correlation coefficient r_xy: {r_xy:.3f}")
