#Instead of doing the %10 and /10 algorithm 
# as I did in a previous problem, I will just convert
# the number into a string and then convert each digit 
# into integers to add them all

strNumber=str(2**1000)
totalsum=0

for element in strNumber:
    totalsum+=int(element)

print(totalsum)
