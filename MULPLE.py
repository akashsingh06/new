# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:24:33 2018

@author: sharda
"""

class A:
    def a(self):
        print("a class")
class B(A):
    def a(self):
        print("b class")
class C(B) :
    def a(self):
        print("c class")
C1=B()
C1.a()