def newEq(theEquation, ans, theTerm, theVar):
    """
      Content under Creative Commons Attribution license CC-BY 4.0, 
      code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

      http://en.wikipedia.org/wiki/MIT_License
      http://creativecommons.org/licenses/by/4.0/

      Created on april, 2018
      Last Modified on: may 15, 2018

      This is a helper function to find step by step the solution
      of any linear equation via operations on both
      sides of the equation. In case of doubt, option 5 can be
      used to check the answer. This also can also be used
      to find solutions to any one variable non-linear equation.
    """
    from sympy import symbols, Eq, solveset, S, sympify
    from sympy import simplify, factor, expand, collect, nsimplify
      
    LHS, RHS = theEquation.split('=')
    LHS = sympify(LHS)
    RHS = sympify(RHS)
    if ans == 1:
         term = sympify(theTerm)
         RHS = nsimplify(RHS + term)
         LHS = nsimplify(LHS + term)
    elif ans == 2:
         term = sympify(theTerm)
         RHS = nsimplify(RHS - term)
         LHS = nsimplify(LHS - term)
    elif ans == 3:
         term = sympify(theTerm)
         #RHS = nsimplify( simplify(factor(RHS * term)) )
         #LHS = nsimplify( simplify(factor(LHS * term)) )
         RHS = nsimplify( simplify(RHS * term) )
         LHS = nsimplify( simplify(LHS * term) )
    elif ans == 4:
         term = sympify(theTerm)
         if term != 0: 
            #RHS = nsimplify( simplify(expand(RHS / term)) )
            #LHS = nsimplify( simplify(expand(LHS / term)) )
            RHS = nsimplify( simplify(RHS / term) )
            LHS = nsimplify( simplify(LHS / term) )
    elif ans == 5:
         theVar = symbols(theVar)
         RHS = nsimplify( simplify(RHS) )
         LHS = nsimplify( simplify(LHS) )
        #RHS = solveset( Eq(LHS, RHS), theVar) ).args[0]
         RHS = list( solveset( Eq(LHS, RHS), theVar) )
         if len(RHS) == 1:
            RHS = RHS[0]
         LHS = theVar 
    else:
         RHS = RHS 
         LHS = LHS
      
    theneweq = '{0} = {1}'.format(LHS,RHS)
    return theneweq
