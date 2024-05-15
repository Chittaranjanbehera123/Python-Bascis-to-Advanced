# Collections: counter, namedtuple, orderDict,defaultdict,deque
from collections import Counter

# Initialize Counter object
a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter)
print(my_counter.most_common(1)[0][0])

# Print the elements of the Counter
print(list(my_counter.elements()))

# Examples2
from collections import namedtuple
point = namedtuple('point','x,y')
pt=point(1, -4)
print(pt.x, pt.y)

# Examples3
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extendleft([4,5,6])
print(d)
d.rotate(-1)
print(d)