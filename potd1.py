# -*- coding: utf-8 -*-
"""
Program to compare between 3 number and print the maximum number.

Algorithms:
    1-ask the user to enter 3 different number
    2-store the numbers in list.
    3-sort the list.
    4-check if the entered number are equal
    5-if yes then print entered number are equal.
    6-otherwise print the last number is the largest.
"""
#define a list
list_=[]

#define 3 numbers
num1=int(input("Enter num 1: "))

num2=int(input("Enter num2: "))

num3=int(input("Enter num3: "))

#add the numbers to the list
list_.append(num1)
list_.append(num2)
list_.append(num3)

#check if the entered number are equal
if (num1==num2==num3):
    print("entered number are equal")
else:
    print(max(list_),"is the largest")