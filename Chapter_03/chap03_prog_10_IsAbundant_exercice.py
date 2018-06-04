'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


from chap03_prog_10_IsAbundant_func import myfuncIsAbundant 

n = 1000
if myfuncIsAbundant(n):
   print('The number {0} is abundant'.format(n))

abundantNumbers = []
i = 1
while i <= n:
   if myfuncIsAbundant(i):
      abundantNumbers = abundantNumbers + [i]
   i = i + 1
print('Between {0} and {1}, there are {2} abundant numbers: '.
                                      format(1,n,len(abundantNumbers)))
print(abundantNumbers)
print (i)
# Between 1 and 1000, there are 246 abundant numbers: 

