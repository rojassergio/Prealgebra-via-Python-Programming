
"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   This program makes a scatter plot of the data 
   in x and y.
"""

import matplotlib.pyplot as plt

x  = [1.5, 2.7, 3.8, 9.5,12.3]
y =  [3.8,-2.4, 0.35,6.2,1.5]

plt.plot(x, y, 'bo', label='This is the red plot legend', lw=2, ms=10)

plt.show()


