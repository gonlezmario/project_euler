#Libraries
import math

#Variables
n=600851475143
possibleFactor=int(math.sqrt(600851475143)) #Assuming n is not a prime already

#Functions
def nPrime(number): #is prime function
    isPrime=True
    for i in range(2,number):
        if number%i==0:
            isPrime=False
    return isPrime

while possibleFactor>0:
    if n%possibleFactor==0 and nPrime(possibleFactor):
        print(possibleFactor)
        break
    else:
        possibleFactor-=1