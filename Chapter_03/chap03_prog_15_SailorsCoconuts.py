"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018

   This program can be used to find solutions to the
   Sailors, Coconuts, and Monkeys popular problem:
      Sources:
      https://wordplay.blogs.nytimes.com/2013/10/07/gardner-2/
      http://mathworld.wolfram.com/MonkeyandCoconutProblem.html
"""
         
N = 0            # Track the trial total number of coconuts
TheNs = []       # A list to keep found solutions
howmanysols = 3  # The number of solutions to find
notfound = True  # A boolean to terminate the loop
while notfound: 
    N = N + 1 # whenever any of the nested IF fails, the flow returns here
    q1 = N - 1
    if q1 % 5 == 0:
       q1 = q1//5 # stage one division
       q2 = 4*q1 - 1
       if q2 % 5 == 0:
          q2 = q2//5 # stage two division
          q3 = 4*q2 - 1
          if q3 % 5 == 0:
             q3 = q3//5 # stage three division
             q4 = 4*q3 - 1
             if q4 % 5 == 0:
                q4 = q4//5 # stage four division
                q5 = 4*q4 - 1
                if q5 % 5 == 0:
                   q5 = q5//5 # stage five division
                   q6 = 4*q5
                   if q6 % 5 == 0:
                      q6 = q6//5 # (last) division at stage six
                      if howmanysols > len(TheNs):
                          TheNs = TheNs + [N]
                      else:
                          notfound = False

print('Found required {0} values for N = {1}'.format(howmanysols, TheNs))


