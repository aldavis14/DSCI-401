#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:32:43 2019

@author: allisondavis
"""

#from basic_examples import * #import everything in basic_examples
#from basic_examples import print_all #imports only print_all-import multiple functions with commas
#import basic_examples #imports basic_functions as a module object 
import basic_examples as bf #imports basic_functions into the aias bf 


#call print_all in bf:
#bf.print_all(55,100,234,899)

#%%

#show examples of sorting:
a=[1,7,3,2,0,11,56,29]
b=list(a)
print(a)
a.sort()
print(a)

print('-----')
print(b)
print(sorted(b))
print(b)

#%% sort tuples

tups=[('a',4),('y',1),('k',12),('m',6)]

print('----Key Sorting Example---Sort by first element in each tuple-')
print(sorted(tups,key=lambda x: x[0]))

print('----Key Sorting Example---Sort by second element in each tuple-')
print(sorted(tups,key=lambda x: x[1]))

#%% Fibonacci Numbers

print('------Fibonacci Numbers Examples-----')
print(bf.fib(1,2,6))
print(bf.fib(1,2,8))
print(bf.fib(1,2,150))

#%%Cartesian Product example
print(bf.Cartesian_Product([1,2,3],[4,5,6]))













