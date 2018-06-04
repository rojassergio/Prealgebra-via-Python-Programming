'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


TheValues = [17, 14, 14, 16, 15, 16, 14, 15, 13, 18, 13]

NumberOfValues = 0
TheAdding = 0

for newValue in TheValues:
   NumberOfValues = NumberOfValues + 1
   TheAdding = TheAdding + newValue

if (TheAdding % NumberOfValues) == 0:
    TheMean = TheAdding//NumberOfValues
    print('The mean of the values is the whole number = {0}'.format(TheMean))
else:
    TheMean = TheAdding/NumberOfValues
    print('The mean of the values IS NOT a whole number = {0}'.format(TheMean))

