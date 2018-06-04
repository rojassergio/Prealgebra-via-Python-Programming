'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


def myfuncPrimeFactors(n):
    """
    This function finds and returns the prime factorization
    of a whole number (excluding zero) via the reiterative division
    method.

    Example of usage:
      getPrimeFactors = myfuncPrimeFactors( 716 )
      print(getPrimeFactors)
    """
    i = 2  
    factors  = []
    while n != 1:
        if (n % i == 0):
          factors = factors + [i]
          n = n//i
        else:
          i = i+1
    return factors

