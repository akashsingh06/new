# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 01:08:49 2018

@author: sharda
"""
class ABC:
    class_var=0
    def __init__(self,var):
       ABC.class_var+=1
       self.var=var
       print("the object variable is:",var)
       print("the class variable is:",ABC.class_var)
    def __del__(self):
     ABC.class_var-=1
     print("the class value is:",ABC.class_var)
       
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
del obj1
del obj2