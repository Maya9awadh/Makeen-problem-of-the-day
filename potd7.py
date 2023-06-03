# -*- coding: utf-8 -*-
"""
Program that is print the more repeted number
"""
lst=[]
print("Enter elements of the list below")
try:
    while True:
        x=int(input('number: '))
        lst.append(x)
except:        
    print(lst)
#print the number that has maximum count
#intialize the most repeted number
i=0
num=lst[0]
for elem in lst:
    curr_frequency = lst.count(elem)
    if(curr_frequency> i):
        counter = curr_frequency
        num = elem
print("The most repeated number is: ",num)