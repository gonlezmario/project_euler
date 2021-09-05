#Variables

term=1
termold=0
totalsum=0

#Loop
while term<4000000:
    if term%2!=0: #Even numbers
        totalsum+=term
    memory=term #Fibonacci algorithm
    term+=termold
    termold=memory

print(totalsum)