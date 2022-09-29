#Evenly divisible function
def evenlyDivisible(num):
    for i in range(1, 21):
        if (num % i != 0):
            return False
    return True

i = 1

while True:
    if(evenlyDivisible(i)):
        sol = i
        break
    else:
        i += 1

print(sol)
