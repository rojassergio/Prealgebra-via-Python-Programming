'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


x = [ 0, 3, 1, 2, 4, 6, 5, 0] # Defines a list holding a few numbers
count = 0 # Initialize a counter to hold the value zero
for i in x:  # start a loop over the list
     y = i//2 # take the exact/inexact result of dividing i by two
     if ((y + 1) == i):   # Applies a conditional IF operation
        count = count + 1 # IF condition is True, update by one count       
count2 = len(x) - count # Can you see why?
s1 = 'In the list, {0} elements (j) '.format(count)
s2 = 'j//2 + 1 == j'
if count == count2:
     s3 = 'satisfies and do not satisfy that '
     print(s1 + s3 + s2)
elif count > count2:
     s3='In the list, more elements (j) satisfy that '.format(count2)
     print(s3 + s2)
else:
     s3 = 'In the list, fewer elements (j) satisfy that '.format(count2)
     print(s3 + s2)

