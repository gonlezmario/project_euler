#Variables
a=1
b=1

#Function
def eq(a,b):
    equation = -1000*a-1000*b+a*b+500000 #Obtained solving for c in a+b+c=1000 and a**2+b**2=c**2 and expanding
    return equation

#Loop
for a in range(500): # a and b as upper limit since if a=500 and b=500 c=0 already
    for b in range(500):
        if eq(a,b)==0:
            finalResult=a*b*(1000-a-b)
            break

print(finalResult)
