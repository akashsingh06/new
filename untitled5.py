# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 10:17:56 2018

@author: sharda
"""
def perfect():
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")