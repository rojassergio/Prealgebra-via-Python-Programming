
"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   This program makes an scatter plot of the data 
   in x and y. It then makes an scatter plot of the data
   in ln(x) and ln(y). The program ends showing the linear
   fit of ln(y) Vs ln(x).
"""

def MakePlot(x, y, xl='R', yl='T', titlel='T Vs R', savel='ThePlanets.png'):
    fig = plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'bo', lw=2, ms=10)
    plt.title(titlel, fontsize = 15)
    plt.xlabel(xl, fontsize = 15)
    plt.ylabel(yl, fontsize = 15)
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    fig.savefig(savel)
    plt.show()

import matplotlib.pyplot as plt
import numpy as np

planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
#---------
# orbit period
T  = [ 88.0/365.3, 224.7/365.3, 365.3/365.3, 687.0/365.3,
       11.86,      29.46,        84.01,       164.8,      248.7] 
#------
# orbit radius
R =  [ 5.79*10**10, 1.08*10**11, 1.49*10**11, 2.28*10**11,
       7.78*10**11, 1.43*10**12, 2.87*10**12, 4.49*10**12, 5.91*10**12] 

#------ Uncomment the next two lines to see the values on the screen
#print('T = ', T)
#print('R = ', R)

# make the data in lists T and R numpy arrays
T = np.array(T)
R = np.array(R)

# Visualize T Vs R
MakePlot(R, T, xl='R', yl='T', titlel='T Vs R', savel='TvsR.png')

# Visualize log(T) Vs log(R)
x = np.log(R) # taking natural log of R values
y = np.log(T) # taking natural log of T values
MakePlot(x, y, xl='ln(R)', yl='ln(T)', 
                     titlel='ln(T) Vs ln(R)', savel='lnTvslnR.png')

# calculate the polynomial fit

z = np.polyfit(x, y, 1) # 1 means fit data to a stright line y = m*x + b
print(z)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

m = '{0:.4f}'.format(z[0])
b = '{0:.4f}'.format(z[1])
print('slope m = ', m)
print('intercept b = ', b)

thetitle = 'ln(T) = m ln(R) + b with m = ' + m + ' and b = ' + b

fig = plt.figure(figsize=(8, 6))
plt.plot(x, y, 'bo', lw=2, ms=10)
plt.plot(x_new, y_new, 'r-', lw=2, ms=10)
plt.title(thetitle, fontsize = 15)
plt.xlabel('ln(R)', fontsize = 15)
plt.ylabel('ln(T)', fontsize = 15)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)
fig.savefig('lnTvslnR_fit.png')
plt.show()


