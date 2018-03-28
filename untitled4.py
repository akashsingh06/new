# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:15:25 2018

@author: sharda
"""
m=[]
for k in range(2,5):
  print("For.. ",k-1,"..matrix")
  l=[]
  for i in range (0,3):
       l1=[]
       for j in range(0,3):
           n=int(input("Enter value:"))
           l1.append(n)
       l.append(l1)
  
  m.append(l)
for i in range(0,len(m)):
    l1=m[0]
    l2=m[1]
    l3=m[2]
for  r in l1:
    print("First Matrix:",r)
for  r in l2:
    print("First Matrix:",r)
for  r in l3:
    print("First Matrix:",r)
 
 