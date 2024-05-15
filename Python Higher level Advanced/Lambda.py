# Lambda arguments: expressions
add10 = lambda x:x+10
print(add10(5))

def add10_func(x):
    return x+10

mult = lambda x,y:x*y
print(mult(2, 7))

# Example2
Points2D = [(1, 2),(15, 1),(5, -1),(10, 4)]

Points2D_sorted=sorted(Points2D, key=lambda x: x[0]+x[1])

print(Points2D)
print(Points2D_sorted)

# Example4
from functools import reduce
a = [1, 2, 3, 4]

product_a=reduce(lambda x,y:x*y,a)
print(product_a)

# Contextmng.py
from threading import Lock
Lock=Lock()

Lock.acquire()
Lock.release()