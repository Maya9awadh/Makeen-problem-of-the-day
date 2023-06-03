# -*- coding: utf-8 -*-
"""
Write a function that contains a variables(length,num)
and returns the multiples of the number and stop in the given length
"""
def Multiples(num,length):
    i=1
    lst=[]
    while i<=length:
        lst.append(num*i)
        i+=1
    return lst
def main():
    l=Multiples(10, 4)
    print(l)
main()