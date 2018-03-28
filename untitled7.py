# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:19:34 2018

@author: sharda
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 23:16:40 2018

@author: sharda
"""
Q=int(input("enter len"))
a=[]
for i in range(Q):
    b=[]
    for j in range(Q):
        g=int(input("enter 1st matrix element"))
        b.append(g)
    a.append(b)
b=[]
for k in range(Q):
    d=[]
    for l in range(Q):
        h=int(input("enter 2nd matrix element"))
        d.append(h)
    b.append(d)
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(Q):
    for j in range(Q):
        for k in range(Q):
            c[i][j]=c[i][j]+a[j][k]+b[k][i]