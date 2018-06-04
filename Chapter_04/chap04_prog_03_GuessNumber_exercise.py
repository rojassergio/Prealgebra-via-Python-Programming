'''
Content under Creative Commons Attribution license CC-BY 4.0, 
code under MIT license (c)2018 Sergio Rojas (srojas@usb.ve) 

http://en.wikipedia.org/wiki/MIT_License
http://creativecommons.org/licenses/by/4.0/

Created on april, 2018
Last Modified on: may 15, 2018
'''

s1=str("\n   Enter 'h' to indicate the guess is too high. \n")
s2=str("   Enter 'l' to indicate the guess is too low.   \n")
s3=str("   Enter 'n' to indicate neither of the above. \n")
text= s1 + s2 + s3

print("\t Please, think of a whole number between 0 and 100 ")
input("\t Hit return to continue " )
high=100+1
low=0
half=(high+low)//2
theinput = input("Is your secret number " + str(half) + "?. " + text)
while theinput != 'n':
    if theinput == 'h':
        high = half
        half = (high + low)//2
    elif theinput == 'l':
        low = half
        half = (high + low)//2
    else:
        tempstr = "\t  *** Your answer '{0}' was not 'h', 'l', or 'c' ***"
        print(tempstr.format(theinput)) 
    theinput = input("Is your secret number " + str(half) + "?. " + text)

print("Game over. Your secret number was: " + str(half))

