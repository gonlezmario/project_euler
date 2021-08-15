# Product of the least common multiples
def isPrime(n): #Includes 1 as prime although it isn't prime!
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def primeFactors(n):
    primeFactorsList=[]
    for i in range(1,int(n**0.5)):
        if isPrime(i):
            primeFactorsList.append(i)
    return primeFactorsList


print(isPrime(17))

