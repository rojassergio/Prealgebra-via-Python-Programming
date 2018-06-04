'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


def myfuncIsPrime( thenumber ):
    """
    This function finds if thenumber is prime or not.
    It is based on the definition of what a prime number is:
    one whose factors are one and itself.

    The function returns True if thenumber is prime, and False otherwise.

    Example of usage:
      getAns = myfuncIsPrime( 6 )
      print(getAns)
    """
    from chap03_prog_08_factor_func import myfuncFactors

    theFactors = myfuncFactors( thenumber )

    if sum(theFactors) == (thenumber + 1):
       return True
    else:
       return False

