# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:53:59 2018

@author: sharda
"""

try:
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[[2,3,4],[5,6,7],[8,9,1]]
    c=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(0,len(a)):
        for j in range(len(a[0])):
            c[i][j]=a[i][j]-b[i][j]
    for r in c:
        print(r)
except EOFError:
    print("Check paranthesis EOF error")
finally:
    print("Program Simulated and Terminated")