#Primality function
def isPrime(n): #Includes 1 as prime although it isn't prime!
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

finalResult=0

#Loop
for i in range(2,2000000):
    if isPrime(i):
        finalResult=finalResult+i #Add all prime numbers

print(finalResult)