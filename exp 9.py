import numpy as np
import pandas as pd

def spearman_rank_correlation(x, y):
  
    rank_x = pd.Series(x).rank()
    rank_y = pd.Series(y).rank()
    
    
    d = rank_x - rank_y
    
   
    d_squared = d ** 2
    sum_d_squared = np.sum(d_squared)
    
    
    n = len(x)
    
    
    r_s = 1 - (6 * sum_d_squared) / (n * (n**2 - 1))
    
    return r_s


study_hours = [2, 4, 6, 8, 10]
exam_scores = [50, 55, 65, 75, 85]


r_s = spearman_rank_correlation(study_hours, exam_scores)
print(f"Spearman's rank correlation coefficient r_s: {r_s:.3f}")
