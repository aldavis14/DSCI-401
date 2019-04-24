#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:58:09 2019

@author: allisondavis
"""
#%%
import pandas as pd
import numpy as np
from statistics import mode

# For Assignment 3 - this is what will go into your "knn.py" file.
class KNN:
    def __init__(self, k, distance_f):
        self.k = k
        self.distance_f = distance_f
    
    def fit(self, x, y):
        if isinstance(x, pd.DataFrame)==True:
            self.x = x.values
        else:
            self.x = x
        if isinstance(y, pd.DataFrame)==True:
            self.y = y.values
        elif isinstance(y, pd.Series)==True:
            self.y = y.values
        else:
            self.y = y
    
    def predict(self, X):
        if isinstance(X, pd.DataFrame):
            self.X = X.values
        else:
            self.X = X
        Y = []
        for row in self.X:
            distances = np.zeros([0,2])
            index = -1
            for row1 in self.x:
                d = self.distance_f(row, row1)
                index += 1
                distances = np.vstack( [distances, np.array([d, int(index)])])
            sorted_distances = distances[distances[:,0].argsort()] #sort distances 
            sorted_k = sorted_distances[:self.k, :] # k shortest distances
            k_indexes = list(sorted_k[:,-1])
            k_indexes = [int(x) for x in k_indexes]
            counts = []
            for n in k_indexes:
                counts.append(self.y[n])
            Y.append(mode(counts))
        
        Y = np.array(Y)
        return Y

