'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

TheValues = [336.1, 346.67, 354.54, 359.9, 338.61, 348.16, 355.2, 360.,
339.32, 349.31, 355.36, 363.13, 350.56, 355.76, 342.62, 351.88,
356.85, 342.88, 351.99, 358.16, 343.44, 352.12, 358.3, 344.32,
352.47, 359.18, 345.03, 353.21, 359.56, 346.5]

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

print('The median = {0}'.format(TheMedian))
In [8]: import numpy as np

In [9]: np.median(TheValues)
Out[9]: 352.05500000000001



