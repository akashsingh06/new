# -*- coding: utf-8 -*-
class abc:
    class_var=0
    def __init__ (self,var):
        abc.class_var+=1
        self.var=var
        print("obejec variable",var)
        print("class variable",abc.class_var)
obj_1=abc(10)
obj_2=abc(20)
obj_3=abc(30)



