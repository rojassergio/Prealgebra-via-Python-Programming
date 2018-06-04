"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

  This program finds the solution of the equation
     7 = x + 9
     b = x + a
  using the bisection of the interval
  [-100,100]
"""

xmin = -100
xmax =  100
maxstep = 150000 # stop is not solution found


b = 7; a = 9
b = 17; a = 19
b = 30; a = 19
b = 0; a = 19
b = 30; a = 0
LHS = b

print("\t The equation is: {0} = x + {1}".format(b, a))
i = 0
nosol = True
while nosol and i < 150000:
   i = i + 1
   x = (xmax + xmin)//2
   RHS = x + a 
   if RHS == LHS:  
      nosol = False
   elif RHS > LHS:
      xmax = x
   else:
      xmin = x
      
if RHS == LHS:
  print('In {0} steps: x = {2} gives RHS = {1} == {3}'.format(i, RHS, x, LHS))
else:
  print('In {0} steps: x = {2} gives RHS = {1} != {3}'.format(i, RHS, x, LHS))


