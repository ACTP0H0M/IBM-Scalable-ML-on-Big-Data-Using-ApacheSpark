# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:03:02 2021

@author: mikep
"""

import numpy as np
from scipy.stats import kurtosis, skew

mean = np.mean([1,2,4,5,34,1,32,4,34,2,1,3])
print('Mean: ' + str(mean))

median = np.median([1,2,4,5,34,1,32,4,34,2,1,3])
print('Median: ' + str(median))

std = np.std([34,1,23,4,3,3,12,4,3,1])
print('Std.dev.: ' + str(std))

kurt = kurtosis([34,1,23,4,3,3,12,4,3,1])
print('Kurtosis: ' + str(kurt))

sk = skew([34,1,23,4,3,3,12,4,3,1])
print('Skewness: ' + str(sk))

lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = [7,6,5,4,5,6,7,8,9,10]
cov = np.cov([lst1,lst2])
print('Covariance: ' + str(cov[0][1]))

corr = cov[0][1] / (np.std(lst1) * np.std(lst2))
print('Correlation: ' +str(corr))