'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018
'''

def myfuncReadInt():
    """
       This function reads a whole number from the user in an
       interactive session. It returns None if data is wrong.
    """
    myitis = True ; count = 1; attempts = 3
    while myitis and count <= attempts:
      try:
         mystr = 'Enter a whole number '
         mystr = mystr + '(attempt {0} of {1}): '.format(count,attempts)
         data = input(mystr)
         data = int(data)
         if data >= 0:
            return data
         else:
            print('\t Negative values are not whole numbers!!!')
            data = None ; myitis = True
            count = count + 1
      except Exception as errorCaptured:
         print("When reading your input, something strange happened:")
         print("\t  *** {0:s} ***".format( str(type(errorCaptured)) ))
         count = count + 1
         data = None ; myitis = True
    return data
 
