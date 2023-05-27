# -*- coding: utf-8 -*-
"""
problem 5,
rotate the list to the left
"""
import collections
rotate=int(input('Enter rotate number: '))
l=collections.deque([1,2,3,4,5])
l.rotate(-rotate)
print(list(l))
