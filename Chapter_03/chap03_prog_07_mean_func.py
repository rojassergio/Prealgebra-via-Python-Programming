'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

def myfuncMean( TheListOfvalues ):
    """ 
       This function computes and returns:
            1.- The mean of a list holding any set of values.
            2.- A message regarding whether the mean is or not a whole number.
       To call this function do:
            thevalues = [1,2,3,4,5]
            meanval, message = myfunc_mean( thevalues )
    """
    NumberOfValues = 0
    TheAdding = 0
    
    for newValue in TheListOfvalues:
       NumberOfValues = NumberOfValues + 1
       TheAdding = TheAdding + newValue
    
    if (TheAdding % NumberOfValues) == 0:
        TheMean = TheAdding//NumberOfValues
        mesg = 'The mean of the values is the whole number = {0}'.format(TheMean)
    else:
        TheMean = TheAdding/NumberOfValues
        mesg = 'The mean of the values IS NOT a whole number = {0}'.format(TheMean)
    return TheMean, mesg 
