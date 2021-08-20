
def collatzSeq(n):
    counterSeq=0
    while n>=2:
        if not n % 2: # n is even
            n//=2
            counterSeq+=1
        else: # n is odd
            n=3*n+1
            counterSeq+=1
    return counterSeq

biggestCounter=1
biggestStartingNumber=1

for i in range(10**6):
    if collatzSeq(i)>biggestCounter:
        biggestCounter=collatzSeq(i)
        biggestStartingNumber=i

print(biggestStartingNumber)
