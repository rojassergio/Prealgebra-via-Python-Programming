'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on january, 2018
Last Modified on: may 15, 2018
'''

# Checking the Python Version installed on this system: 
import sys
import platform
print("\n")
print("Python distribution details: ")
print(sys.version)
print("\n")
print(str("Installed Python Version is: ")+str(platform.python_version()))

# Checking the Numpy Version installed on this system: 
try:
  import numpy
  print(str("Installed Numpy version is: ")+str(numpy.__version__))
except ImportError:
  sys.exit("Error : Numpy can not be imported or is not installed.")

# Checking the Scipy Version installed on this system: 
try:
  import scipy
  print(str("Installed Scipy version is: ")+str(scipy.__version__))
except ImportError:
  sys.exit("Error : Scipy can not be imported or is not installed.")

# Checking the Ipython Version installed on this system: 
try:
  import IPython
  print(str("Installed IPython version is: ")+str(IPython.__version__))
except ImportError:
  sys.exit("Error : IPython can not be imported or is not installed.")

# Checking the Matplotlib Version installed on this system: 
try:
  import matplotlib
  print(str("Installed Matplotlib version is: ")+str(matplotlib.__version__))
except ImportError:
  sys.exit("Error : Matplotlib can not be imported or is not installed.")

# Testing Pandas
try:
  import pandas
  print(str("Installed Pandas version is: ")+str(pandas.__version__))
except ImportError:
  sys.exit("Error : Pandas can not be imported or not installed.")

print("\n")
print("\t    Necessary tools are installed. This system seems to be ready")
print("\t    to crunch numbers via python ...")

print("\n")
print("\t  There are some tests one can run to check...")
print("\t  if the installed packages work  correctly...")
print("\t  Each test takes some time. ...")

# This makes input to work in Python 2.x.
try: 
   input = raw_input
except NameError: 
   pass

print("\n")
print("\t  Would you like to run the NUMPY basic test suite...")
ans = input("For yes, enter y and hit return: ")
if ans=='y':
   print(str("Running some Numpy tests: "))
   #python -c "import numpy; numpy.test()"
   numpy.test()

print("\n")
print("\t  Would you like to run the SCIPY basic test suite...")
ans = input("For yes, enter y and hit return: ")
if ans=='y':
  print(str("Running some Scipy tests: "))
  #python -c "import scipy; scipy.test(); 
  scipy.test()

print("\n")
print("\t  Would you like to run the IPYTHON basic test suite...")
ans = input("For yes, enter y and hit return: ")
if ans=='y':
  print(str("Running some Ipython tests: "))
  # python -c "import IPython; IPython.test()"
  IPython.test()
