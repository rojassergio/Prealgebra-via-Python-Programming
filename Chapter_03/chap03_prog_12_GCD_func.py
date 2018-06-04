'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

def myfuncGCD( listOfnumbers ):
    """
    This function finds and returns the greatest common divisor
    of a set of whole numbers (excluding zero) via the
    factors listing method.
    

    Example of usage:
      getGCD = myfuncGCD( [716, 1266, 1490, 1568] )
      print(getGCD)
    """
    from chap03_prog_08_factor_func import myfuncFactors

    if len(listOfnumbers) == 1:
       return True, listOfnumbers[0]

    listOfnumbers.sort() 

    smallestNumFactors  = myfuncFactors( listOfnumbers[0] )
    i = 1
    othersNumFactors = []
    while i < len( listOfnumbers ):
      othersNumFactors = othersNumFactors + [myfuncFactors( listOfnumbers[i] )]
      i=i+1
        
    gcd = []
    for y in smallestNumFactors:
       itis = True
       for z in othersNumFactors:
           if y in z:
              itis = itis and True
           else:
              itis = itis and False
       if itis:
           gcd = gcd + [y]

    return max(gcd)

