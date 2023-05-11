# -*- coding: utf-8 -*-

"""
program to calculate the length and slop 
of each vector in matrix.

"""
#import library
import numpy as np
import math as m

#intialize a matrix
matrix=[[-10,20,-10,-18],
        [-10,20,0,3],
        [0,3,8,17],
        [8,17,10,-16],
        [10,-16,-10,-18]]
#transfer the matrix to np array
a=np.array(matrix)


#initialize list to store all y.
y=[]
print("        Length" "          ","Slop")
#iterate over the row of matrix
for i in range(5):
        #calculate the length of vector
        l=m.sqrt((a[i][3]-a[i][1])**2 +(a[i][2]-a[i][0])**2)
        print("S"+str(i),' ',l,end=' ')
        #calculate the slope of vector
        s=(a[i][3]-a[i][1])/(a[i][2]-a[i][0])
        #add the slop to the list
        
        print(' ',s)
       
        
        #add all y to the list
        y.append(a[i][1])
        y.append(a[i][3])
          
#print(length)   
#print(slop)
print("max y is: ",max(y))
print("min of y:",min(y))
