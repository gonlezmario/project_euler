import math

def eulerSum(n): #Euler's formula to find the total sum of all integers up to an integer n
    eulerSum=int(n*(n+1)/2)
    return eulerSum

def get_factors(n):
    sum=0
    for i in range(1, math.ceil(math.sqrt(n))): #All unique factors are smaller than sqrt(n)
        if n % i == 0:
            sum+=2 #Count also the duplicate factor
    return sum

i=1
factorLimit=500

while get_factors((eulerSum(i)))<factorLimit:
    i+=1

print(eulerSum(i))