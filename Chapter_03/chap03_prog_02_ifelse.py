'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

x = [ 0, 3, 1, 2, 4, 6, 5, 0] # Defines a list holding a few numbers

count = 0  # Initialize a counter to hold the value zero

count2 = 0 # Initialize a counter to hold the value zero

for i in x:  # start a loop over the list
    y = i//2 # take the exact/inexact result of dividing i by two
    if ((y + 1) == i):   # Applies a conditional IF operation
        count = count + 1 # IF condition is True, update by one count 
    else:
        count2 = count2 + 1 # IF condition is False, update by one count2

s1 = 'In the list, {0} elements (j) satisfies that '.format(count)

s3 = 'In the list, {0} elements (j) DO NOT satisfy that '.format(count2)

s2 = 'j//2 + 1 == j'

print(s3 + s2) ; print(s1 + s2)

