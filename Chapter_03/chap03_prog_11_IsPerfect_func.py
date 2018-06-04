'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

def myfuncIsPerfect( thenumber ):
    """
    This function finds if thenumber is perfect or not.
    It is based on the definition of what a perfect number is:
    one whose proper divisors adds up to exactly the number itself.

    The function returns True if thenumber is perfect, and False otherwise.

    Example of usage:
      getAns = myfuncIsPerfect( 6 )
      print(getAns)
    """
    from chap03_prog_08_factor_func import myfuncFactors

    factors = myfuncFactors( thenumber )
    ProperDivisorsAdd = sum(factors) - thenumber
   
    if ProperDivisorsAdd == thenumber:
        return True
    else:
        return False

