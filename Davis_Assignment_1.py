#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:48:41 2019

@author: allisondavis
"""

# I. Flatten
def flatten(A):
    if A == []:
        return A
    if type(A[0]) == list:
        return flatten(A[0]) + flatten(A[1:])
    return A[:1] + flatten(A[1:])

#%% II. Power Set
def powerset(B):
    if len(B) == 0:
        return [[]]
    ps = powerset(B[1:])
    return ps + [[B[0]] + i for i in ps]

#%% III. All Permutations
def all_perms(C):
    if len(C)<=1:
        return [C]
    final=[]
    for i in all_perms(C[1:]):
        for j in range(len(C)):
            final.append(i[:j]+[C[0]]+i[j:])
    return final

#%% IV. Number Spiral 
def spiral(n, end_corner):
    if n == 0:
        return 0 
    







