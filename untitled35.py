# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:55:33 2018

@author: sharda

a=[6,4,5,8,9]
b=a[0]
for i in range(1,len(a)):
    if a[i]>b:
        b=a[i]
print("maximum number is=",b)
print(sum(a))"""



def max(a):
    b=a[0]
    for i in range(1,len(a)):
        if a[i]>b:
            b=a[i]
    return(b)
a=[46,2168,165798,3121,16456,1654,3586,3121,324156]
print(max(a))