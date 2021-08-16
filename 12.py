def eulerSum(n):
    eulerSum=int(n*(n+1)/2)
    return eulerSum

def factorCounter(n):
    counter=1 #Count as factor the number itself
    for i in range(1,n):
        if n%i==0:
            counter+=1
    return counter

#while factorCounter(eulerSum(number))<500:
   #number+=1

print(factorCounter(eulerSum(7)))
