
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

x  = [1.5, 2.7, 3.8, 9.5,12.3]
y =  [3.8,-2.4, 0.35,6.2,1.5]

fig = plt.figure(figsize=(8, 6))
plt.plot(x, y, 'bo', label='Write the plot legend', lw=2, ms=10)
plt.title('The plot title', fontsize = 10)
plt.xlabel('The horizontal (x-axis) label', fontsize = 12)
plt.ylabel('The vertical (y-axis) label', fontsize = 15)
plt.xticks([-4,5,14], fontsize = 20)
plt.yticks(fontsize = 20)
plt.legend(loc='best')
fig.savefig("TheSavedFig.png")
plt.show()


