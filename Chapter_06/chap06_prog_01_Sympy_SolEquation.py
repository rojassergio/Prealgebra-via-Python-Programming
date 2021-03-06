"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

  This program finds the solution of the equation
     3/5 = 5.2x + 9
"""
from sympy import symbols, Eq, solveset, S

x = symbols('x')

LHS = S('3')/5
RHS = 5.2*x + 9

thesol = list( solveset( Eq(LHS, RHS), x) )
#print('The found solution is x =', thesol[0])

# Check the found solution by substitution
newLHS = LHS - RHS #rearrange the equation to read: LHS - RHS = 0
#print('newLHS =', newLHS)

newLHS = newLHS.subs(x, thesol[0])
if newLHS.simplify() < 1e-15:
    print('x = {2} is solution of {0} = {1}'.format(LHS,RHS,thesol[0]))

