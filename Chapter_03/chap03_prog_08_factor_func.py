'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


def myfuncFactors( thenumber ):
    """
    This function finds and returns in a list all the Factors of 
    thenumber, including itself.

    Example of usage:
      getfactors = myfuncFactors( 6 )
      print(getfactors)
    """
    ListOfFactors = []
    n = 1
    while n <= thenumber:
        temp = thenumber % n
        if temp == 0:
           ListOfFactors = ListOfFactors + [n]
        n = n + 1
    return ListOfFactors

