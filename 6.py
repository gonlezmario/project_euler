#Variables
sumOfSquares=0
squaredSum=0
n=100

#Loops
for i in range(1,n+1): 
    squaredSum+=i
squaredSum*=squaredSum #square out of loop

for i in range(1,n+1):
    sumOfSquares+=i**2 #square inside loop

print(squaredSum-sumOfSquares)

