'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

TheValues = [17, 14, 14, 16, 15, 16, 14, 15, 13, 18, 13, 16]

holdvals = []
for j in TheValues:
    temp = 0
    for k in TheValues:
       if j == k:
          temp = temp + 1
    holdvals.append(temp)

themax = max( holdvals ) 

MostRepeatedVals = []
for k in range( len(holdvals) ):
     if holdvals[k] == themax:
         MostRepeatedVals.append( TheValues[k] )

for k in MostRepeatedVals:
  MultiMode  = 0
  for j in MostRepeatedVals:
    if j != k:
       MultiMode = MultiMode + 1 

if MultiMode == 0:
   print('The mode of the data set is unique:')
   print('   Value {0} is repeated {1} times.'
                     .format(MostRepeatedVals[0], len(MostRepeatedVals) ))
elif MultiMode == (len(MostRepeatedVals)-1):
   print('The data set has no mode')
else:
    print('The mode of the data set is not unique:')
    different = MostRepeatedVals.copy()
    pairs = []
    while different: # True as long as list different has elements
         i=0
         l = different[0] 
         temp = []
         for k in different:
             if k != l:
                 temp = temp + [k]
             else:
                 i = i + 1
         pairs = pairs + [[l, i]] 
         different = temp
    for i in pairs:
         print('   Value {0} is repeated {1} time(s).'.format(i[0], i[1]))

