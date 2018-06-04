'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''

def myfuncPrimeSieve(n):
    """
    This function generates and returns prime numbers from 2 up to n
    via the Sieve of Eratosthenes algorithm.

    Example of usage:
      getAns = myfuncPrimeSieve( 20 )
      print(getAns)
    """
    thelist = list(range(3, n, 2)) #generates odd numbers starting from 3
    theprimes = [2]
    while thelist: # True as long as list thelist has elements
        temp = thelist.pop(0)
        theprimes = theprimes + [temp]
        if (temp*temp > n):
           theprimes = theprimes + thelist
           thelist = []
        else:
            for x in thelist:
                if (x % temp) == 0:
                   thelist.remove(x)
    return theprimes  

