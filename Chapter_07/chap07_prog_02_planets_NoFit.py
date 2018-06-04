
"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   This program makes an scatter plot of the data 
   in x and y.
"""

import matplotlib.pyplot as plt
def yinvsquared(y):
  return 1./y**2

def a(r,T):
  import numpy as np
  w = 2*np.pi/T
  return r*w**2

label = ['Mercury',
'Venus',
'Earth',
'Mars',
'Jupiter',
'Saturn',
'Uranus',
'Neptune',
'Pluto']
T  = [ 
88.0/365.3, 
224.7/365.3, 
365.3/365.3,
687.0/365.3,
11.86,
29.46,
84.01,
164.8,
248.7] #orbit period
R =  [
5.79*10**10,
1.08*10**11,
1.49*10**11,
2.28*10**11,
7.78*10**11,
1.43*10**12,
2.87*10**12,
4.49*10**12,
5.91*10**12] #Orbit radius
print('T = ', T)
print('R = ', R)
import numpy as np
# T = np.array(T)
# R = np.array(R)

#a = r*w**2
#1/r**2
twoPi = 2*np.pi
R2inv = []
a = []
for i in range(len(R)):
    #R[i] = R[i]/10**12
    #R2inv = R2inv + [  1.0/R[i]**2  ]
    #a     = a + [  R[i]*( (twoPi/T[i])**2 )  ]
    R2inv = R2inv + [ np.log( 1.0/R[i]**2 ) ]
    a     = a + [ np.log( R[i]*( (twoPi/T[i])**2 ) ) ]
     
x = a
y = R2inv
print('x = log(a) = ', a)
print('y = log(R2inv) = ', R2inv)
   

fig = plt.figure(figsize=(8, 6))
plt.plot(x, y, 'bo', label='Write the plot legend', lw=2, ms=10)
plt.title('The plot title', fontsize = 10)
plt.xlabel('The horizontal (x-axis) label', fontsize = 12)
plt.ylabel('The vertical (y-axis) label', fontsize = 15)
#plt.xticks([-4,5,14], fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(loc='best')
fig.savefig("FigThePlaets.png")
plt.show()


