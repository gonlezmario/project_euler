#Variables
counter=0
number=1

#Function
def isPrime(n): #Includes 1 as prime although it isn't prime!
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

#Loop
while counter<10001:
    number+=1 # 1 isn't checked as prime
    if isPrime(number):
        counter+=1

print(number)
