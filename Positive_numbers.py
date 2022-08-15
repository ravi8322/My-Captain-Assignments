# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 19:37:08 2022

@author: RAVI TEJ
"""

list1=[]
n=int(input("Enter size of list1 "))

for i in range(0,n):
    a=int(input("Enter element of list1 "))
    list1.append(a)
print("list1= ",list1,"Output1: ")
list1=[num for num in list1 if num >= 0]
print(list1)

list2=[]
m=int(input("Enter size of list2 "))
for j in range(0,m):
     b=int(input("Enter element of list2 "))
     list2.append(b)
print("list2= ",list2,"output2: ")
list2=[num for num in list2 if num >= 0]
print(list2)
