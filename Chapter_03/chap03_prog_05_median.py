'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


TheValues = [17, 14, 14, 16, 15, 16, 14, 15, 13, 18, 13]

TheValues.sort()

NumberOfValues = len(TheValues)

if NumberOfValues == 0:
   print(' List of values in empty ')
elif NumberOfValues == 1:
   TheMedian = TheValues[ 0 ]     # The only element in the list
elif (NumberOfValues % 2) == 1:   # Check if the number of values is odd
   temp = NumberOfValues//2
   TheMedian = TheValues[ temp ]
else:
   temp = NumberOfValues//2
   TheMedian = (TheValues[ temp ] + TheValues[ temp - 1 ])/2

print('The median of the set of values is: {0}'.format(TheMedian))

