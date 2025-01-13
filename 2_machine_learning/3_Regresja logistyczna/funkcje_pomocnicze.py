import numpy as np

def find_outliers(x, a= 1.5):
    q1,q3 = np.quantile(x,[0.25,0.75])
    iqr = q3 - q1
    x_min = q1 - a * iqr
    x_max = q3 + a * iqr
    return (x< x_min) | (x > x_max)