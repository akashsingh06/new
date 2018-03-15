# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 02:01:43 2018

@author: sharda
"""

import cal


print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=input("enter choice(1/2/3/4):")
num1=int(input("enter first num:"))
num2=int(input("enter second num:"))

if choice=='1':
   print(num1,"+",num2,"=", cal.add(num1,num2))
elif choice=='2':
   print(num1,"-",num2,"=",cal.subtract(num1,num2))
elif choice=='3':
   print(num1,"*",num2,"=",cal.multiply(num1,num2))
elif choice=='4':
   print(num1,"/",num2,"=",cal.divide(num1,num2))
else:
   print("its not present")