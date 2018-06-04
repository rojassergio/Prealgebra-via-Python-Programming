"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018

   This program finds the algebraic solution of the equation
   a*x + b = c*x + d
"""

from sympy import symbols, Eq, solveset
x, a, b, c, d = symbols('x, a, b, c, d')

LHS = a*x + b
RHS = c*x + d

thesol = list( solveset( Eq(LHS, RHS), x) )

#rearrange the equation to read: LHS - RHS = 0
newLHS = LHS - RHS

newLHS = newLHS.subs(x, thesol[0])

if newLHS.simplify() == 0:
   print('The solution of {0} = {1}, is x = {2}'.format(LHS,RHS,thesol[0]))

