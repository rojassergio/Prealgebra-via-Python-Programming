"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   With this program you can play the 'Guess two-digits' math game.
   The computer ask you two enter a three digit number
   After computing the involved operations (see details on chapter 2)
   you should guess two digits after the computer tells you
   one digit (see chapter 2 for a detailed discussion of the problem).
"""
from chap04_prog_01_TryExcept import myfuncReadInt

print('Step 1.- Reading a 3-digit number:\n\t',end='')
thenumber = myfuncReadInt()
if thenumber == None:
   print('\t *** You did not entered a valid number ***')
else:
   temp = str(thenumber)
   if len(temp) == 3:
       print('Step 2.- Computing the reverse number')
       reversenum = temp[::-1]
       reversenum = int(reversenum)
       print('Step 3.- Computing the difference of the two numbers')
       difference = abs(reversenum - thenumber)
       tempstr = 'Step 4.- The number in the ones place = {0}'
       print(tempstr.format(str(difference)[-1]))
       print('Step 5.- Please, guess the remainder digits in order:\n\t',end='')
       guesstheothertwo = myfuncReadInt()
       if guesstheothertwo == None:
          print('\t *** You did not entered a valid number ***')
       else:
          if difference == 0:
             difference = '000'
          elif difference == 99:
             difference = '099'
          else:
             difference = str(difference)
          GuessShouldBe = int(difference[0]+difference[1])
          temp = guesstheothertwo - GuessShouldBe
          if temp == 0:
             print('Step 6.- Your guess is right')
          else:
             thestr = 'Step 6.- Your guess {0} is wrong. The right value is {1}'
             print(thestr.format(guesstheothertwo, GuessShouldBe))
   else:
        print('You entered the value: {0}'.format(thenumber))
        print('\t That is not a 3-digit number !!!')
