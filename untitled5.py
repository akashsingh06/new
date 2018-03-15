# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:17:34 2018

@author: sharda
"""

data=[]
for i in range(10):
    l={}
    for i in range(5):
        name=input("name")
        l["name"]=name
        roll no=input("roll no")
        l["roll no"]=roll no
        course=input("course")
        l["course"]=course
        address=input("address")
        l["address"]=address
        mobile no=input("mobile no")
        l["mobile no"]=input("mobile no")
        cgpa=input("cgpa")
        l["cgpa"]=input("cgpa")
        data.append(l)
        