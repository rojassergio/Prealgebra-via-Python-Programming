"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

  This program finds the solution of any equation
  Depending how you write your equation,
  the answer could be a rational or a real number. 

  The trick to find rational solution to equations is to
  write at least one numerical value as fractions using 
  the SymPy S function

Author: Sergio Rojas
Licensing: code distributed under the GNU LGPL license.
Code version as of March 23, 2018
"""
#from sympy import symbols, Eq, solveset, S, sympify
from sympy import *
thevar = input('Enter the variable name (i.e. x, y, z): ')

thevar = symbols(thevar) # make the given variable a SymPy symbol

message = \
" *=========\n \
*  Input the part of your equations as requested \n \
*  If your equation looks like: (3/2){0} - 8 = 7{0} + 5 \n \
*  LHS = (3/2){0} - 8, and you should enter for it: (3/2)*{0} - S('8') \n \
*  RHS =     7{0} + 5, and you should enter for it: 7*{0} + S('5') \n \
*  If you write your equation in a text editor, copy and paste might work. \n \
*========="
print(message.format(thevar))
ans = True
while ans:
   LHS = input('Enter the LHS of the equation: ')
   print('\t You entered LHS = ', LHS)
   RHS = input('Enter the RHS of the equation: ')
   print('\t You entered RHS = ', RHS)
   try:
      LHS = sympify(LHS)  # sympify makes a function from an string
      LHS.subs(thevar, 2) # check evaluating the function with a number (2)
      RHS = sympify(RHS)  # sympify makes a function from an string
      RHS.subs(thevar, 2) # check evaluating the function with a number (2)
      ans = False
   except Exception as errorCapturado:
      ans = True
      print('\t Something is wrong with the giving inputs !!!')
      print('\t Please, try again:')

LHS = nsimplify(LHS)
RHS = nsimplify(RHS)

thesol = list( solveset( Eq(LHS, RHS), thevar) )
#print('thesol =', thesol)

theEq = LHS - RHS #rearrange the equation to read: LHS - RHS = 0
#print('theEq =', theEq)

checkSol = []
for sol in thesol:
   temp = theEq.subs(thevar, sol)
   temp = temp.simplify()
   checkSol = checkSol + [temp]

if sum(checkSol) < 1e-14:
    print('Solution(s) of {0} = {1}:'.format(LHS,RHS))
    for sol in thesol: 
        print('\t {0} = {1} = {2}\n'.format(thevar, sol, N(sol)))
else:
    print('Solution(s) found were (check them by substitution): ')
    for sol in thesol: 
        print('\t {0} = {1} = {2}\n'.format(thevar, sol, N(sol)))

