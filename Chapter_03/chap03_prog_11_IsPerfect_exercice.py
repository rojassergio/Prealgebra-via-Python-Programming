'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on march, 2018
Last Modified on: may 15, 2018
'''


from chap03_prog_11_IsPerfect_func import myfuncIsPerfect 

n = 1000
if myfuncIsPerfect(n):
   print('The number {0} is perfect'.format(n))

perfectNumbers = []
i = 1
while i <= n:
   if myfuncIsPerfect(i):
      perfectNumbers = perfectNumbers + [i]
   i = i + 1
print('Between {0} and {1}, there are {2} perfect numbers: '.
                                      format(1,n,len(perfectNumbers)))
print(perfectNumbers)
print (i)
# Between 1 and 1000, there are 246 perfect numbers: 

