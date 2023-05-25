# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:03:56 2023

@author: mayaa
"""
l=[]
print("Enter elements of the list ")
try:
    while True:
        x=int(input(': '))
        l.append(x)
except:        
    print(l)
print()
l1=l[::-1]

count=0
for i in range(len(l)):
    if((sum(l[:i])==sum(l[i:])) or (sum(l1[:i])==sum(l1[i:]))):
        count=1
    else:
        count=0
if count==1:
    print('True')
else:
    print('False')