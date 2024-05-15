# Sets in Python
# Set: unordered, mutuable no duplicates
myset = {1,2,3,1,2}
print(myset)

myset = set("Hello")
print(myset)

# Example2
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u=odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

SetA={1,2,3,4,5,6,7,8,9}
SetB={1,2,3,10,11,12}

diff=SetB.difference(SetA)
print(diff)


SetA = {1,2,3,4,5,6}
SetB = SetA

SetB.add(7)
print(SetB)
print(SetA)