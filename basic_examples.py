#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:03:51 2019

@author: allisondavis
"""
from functools import reduce
#%%
#Some basic illustrations of Python concepts.

#illustrates optional/default args
def print_all(a,b,c=1,d=2):
    print(a)
    print(b)
    print(c)
    print(d)
    
#illustrates optional/unbounded args
def print_optional(a,b,*c):
    print(a)
    print(b)
    print(c)
    
#%%
list(map(lambda x: x+1, [1,2,3]))

#%%
starts_with_a=lambda x: x.lower().startswith('a')

fruits=['grapes','apples','bananas','apricots','blueberries']

list(filter(starts_with_a,fruits))
#%%

[x for x in fruits if starts_with_a(x)]
#%%
import functools as f
f.reduce(lambda x,y: x+y, [1,2,3,4,5,6,7,8,9,10])

product= lambda elements: reduce(lambda y,z: y*z, elements)

#%% Compute the nth Fibonacci number for arbitraty first and second elements.
#cache saves memory and time
def fib(a,b,n, cache={}):
    if n in cache:
        return cache[n]
    if n==1:
        return a
    if n==2:
        return b
    else:
        cache[n]= fib(a,b,n-1, cache)+fib(a,b,n-2, cache)
        return cache[n]

#%% Cartesian Product (non-recursive)
def cp(A,B):
    p=[]
    for i in A:
        for x in B:
            p.append((i,x))
    return p

#%% Cartesian Product (recursive) -with for loop
def Cartesian_Product(*lists):
    if len(lists)==1:
        return [[x] for x in lists[0]]
    else:
        rest=Cartesian_Product(*lists[1:])
        cp=[]
        for i in lists[0]:
            for j in rest:
                cp.append([i]+j)
        return cp
#%%Cartesian Product (recursive) -with reduce
def cartesian_product(*lists):
    if len(lists)==1:
        return [[x] for x in lists[0]]
    else:
        rest=Cartesian_Product(*lists[1:])
        return reduce(lambda x,y:x+y,[[[i]+j for j in rest] for i in lists[0]]) #functional way
        
        
        
#%% Cartesian product example
L=[[1,2,3],[4,5,6],[7,8,9]]

Cartesian_Product(*L)
#%%
cartesian_product(*L)

#%% Generate all unique combinations of elements, taken k at a time
def gen_combs(elems, k):
    if k==len(elems):
        return [elems]
    if k==1:
        return [[x] for x in elems]
    else:
        return [[elems[0]]+ c for c in gen_combs(elems[1:],k-1)]+gen_combs(elems[1:],k)
    
#gen_combs always returns a list of combinations
#%% generate combinations examples
gen_combs(['a','b','c','d'],3)
#gen_combs(list(range(10)),4)




