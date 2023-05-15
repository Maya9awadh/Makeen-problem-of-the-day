# -*- coding: utf-8 -*-
"""
Python program that print the first un repeated number in array
"""
#first, define a function to count 
#cccurances of element in arrray

arr=[1,2,7,8,2,1]

def count_(array,elm):
    count=0
    for i in range(len(array)):
        if(array[i]==elm):
            count=count+1
    return count

#the we check the count of each element and 
#print the first un repeated number
for i in arr:
    if(count_(arr, i)==1):
        print(i)
        break
