import math

n=20+20#All routes must have a (20x20) length (Manhattan distance)
#It's only possible to move in 2 directions, right or down
k=n//2 #We can represent a direction in a base 2 system (binary)

#Since the route must start in one corner and end in the opposite 
# there will be exactly 20 0's and 20 1's in every combination

# Using combinatorics without repetition the number of possible combinations is
# with a length of n bits divided by groups of k elements
# C_nk=n!/(k!*(n-k)!#

c_nk=int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
print(c_nk)
