# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:31:25 2018

@author: sharda
"""

a=[2,8,6,4]
for i in range (0,len(a)):
     for j in range(0,len(a)):
       if a[j]>a[j+1]:
         c=a[j]
         a[j]=a[j+1]
         a[j+1]=c
print(a)

                
        
    