# coding: utf-8
x = [ 0, 3, 1, 2, 4, 6, 5, 0] # Defines a list holding a few numbers
count = 0 # Initialize a counter to hold the value zero
for i in x:  # start a loop over the list
    y = i//2 # take the exact/inexact result of dividing i by two
    if ((y + 1) == i):    # Applies a conditional IF operation
        count = count + 1 # IF condition is True, update by one count
        
s1 = 'In the list, {0} elements (j) satisfies that '.format(count)
s2 = 'j//2 + 1 == j'
print(s1 + s2)
