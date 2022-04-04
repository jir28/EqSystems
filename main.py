#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:23:31 2022

@author: jair
"""

import numpy as np
import copy

def permutations(n):
    arr = [x for x in range(n)]
    result =[]
    dfs(arr,0,len(arr),result)
    return result

def dfs(arr, begin, end,result):
    if begin == end:
        result.append(copy.deepcopy(arr))
        pass
    else:
        for i in range(begin,end):
            arr[i],arr[begin] = arr[begin],arr[i]
            dfs(arr,begin+1,end,result)
            arr[i],arr[begin] = arr[begin],arr[i]
            pass
        pass

def inverse(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                count+=1
                pass
            pass
        pass    
    return count

def det(matrix):
    if matrix.shape[0]!=matrix.shape[1]:
        print('¡Esta matriz no es una matriz cuadrada! ')
        return
    permutation = permutations(matrix.shape[0])
    permutation = np.array(permutation)
    result = 0
    for i in range(len(permutation)):
        a = 1
        for j in range(matrix.shape[0]):
            a*=matrix[j][permutation[i][j]]
        result += pow(-1,inverse(permutation[i]))*a
    return result


def cramer(d,b):
    if d.shape[0]!=d.shape[1]:
        print('¡Esta matriz no es una matriz cuadrada! ')
        return
    if det(d) == 0:
        print('Coeficiente de matriz cuadrada es 0')
        return
    d_i = []
    for i in range(b.shape[0]):
        d_i.append(copy.deepcopy(d))
        d_i[i][:,i] = b
        pass
    x = []
    for i in range(b.shape[0]):
        x.append(det(d_i[i]) / det(d))
    print(x)
    


d = np.array([[4,-1,0,-1,0,0,0,0,0],[-1,4,-1,0,-1,0,0,0,0],[0,-1,4,0,0,-1,0,0,0],[-1,0,0,4,-1,0,-1,0,0],[0,-1,0,-1,4,-1,0,-1,0],[0,0,-1,0,-1,4,0,0,-1],[0,0,0,-1,0,0,4,-1,0],[0,0,0,0,-1,0,-1,4,-1],[0,0,0,0,0,-1,0,-1,4]])
b = np.array([40,30,40,10,0,10,30,20,30])
cramer(d,b)
