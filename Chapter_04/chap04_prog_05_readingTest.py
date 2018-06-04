"""
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018

   This program illustrates how to read any text file containing
   columns of data separated by white spaces, having the
   first row as header.
"""
thefile = 'chap04_write_test_file.txt'
try:
   with open(thefile, 'rt') as openedFile: 
       data = []
       for row in openedFile:
           print('Read line from file       = ',row,end='')
           row = row.strip().split(' ')              
           print('strip-split processed row = ',row)
           while '' in row:
              row.remove('')
           print("removed '' processed row = ",row)
           data = data + [row]
           print('\n')
except Exception as errorCapturado:
     import sys
     print("\t The following error happened when opening the file")
     print("\t *** {0} ***".format(type(errorCapturado)))
     sys.exit(1)

row = 1
while row < len(data):
    i = 0
    while i < len(data[row]):
        data[row][i] = int(data[row][i]) 
        i = i + 1
    row = row + 1

print('Data read in a list: ')
for i in data:
   print(i)

