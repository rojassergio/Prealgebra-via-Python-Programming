
"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   This program illustrates how to write data to a file. If the file exist
   it will be overwritten and the the existing data will be lost
"""
thefile = 'chap04_write_test_file.txt'
colsLabel = ['x', 'x*x', 'x*x*x']
values = [ [1, 1, 1], [2, 4, 8] ]
try:
   with open(thefile, 'wt') as openedFile:
       for cols in colsLabel:
           openedFile.write('{0},'.format(cols))
       openedFile.write('\n')
       for cols in values:
           for rows in cols:
               openedFile.write('{0},'.format(rows))
           openedFile.write('\n')
except Exception as errorCapturado:
     print("\t The following error happened when opening the file")
     print("\t *** {0} ***".format(type(errorCapturado)))

# The next instruction shows that the opened file was closed
# This line should be deleted
# print(openedFile.closed)
