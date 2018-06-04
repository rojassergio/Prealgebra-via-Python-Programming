
"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   Use this program to read a set of whole numbers
   to be assignned to the list 'thenumbers'. You could them
   use that list of values as input to other program.
""" 
from chap04_prog_01_TryExcept import myfuncReadInt

myitis = True
thenumbers = []
while myitis != None:
   print('\t Reading a new number (to exit hit return 3 times)')
   print('\t ',end='')
   myitis = myfuncReadInt()
   if myitis != None:
       thenumbers = thenumbers + [myitis]
   else:
       print('\t *** EXITING THE READING ***')

print(thenumbers)

