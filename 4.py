#Variables
biggestdigit1 = biggestdigit2 = 999

#Functions
def numberReverse(number): #function which reverses the digits of any given number
    reverseNumber=0
    indexedNumber=number
    while indexedNumber>0:
        digit=indexedNumber%10
        indexedNumber//=10
        reverseNumber=digit+reverseNumber*10
    return reverseNumber


def solutionMatrix():
    for i in range(biggestdigit1,0,-1):
        j=biggestdigit2
        while i < biggestdigit1:
            i+=1
            if i*j==numberReverse(i*j): #if a number is palindromic, its reverse is equal to the number itself
                return(i*j)
            else:
                j-=1

print(solutionMatrix())