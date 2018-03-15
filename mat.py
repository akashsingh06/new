# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:13:48 2018

@author: sharda
"""

mat=[]
for j in range(n):
    a=[]
    for i in range(n):
        value=int(input("enter the values of first matrix:"))
        a.append(value)
        mat.append(a)
mat2=[]
for k in range(n):
    b=[]
    for z in range(n):
        value2=int(input("enter the value of second mat:"))
        b.append(value2)
        mat2.append(b)
        
c=[0]*n
for i in range(n):
    c[i]=[0]*n
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]=c[i][j]+mat[i][k]*mat2[k][j]
for i in range(n):
   print(c[i])                  