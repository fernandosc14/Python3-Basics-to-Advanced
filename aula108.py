# Count é um interador infinito
from itertools import count

c1 = count(1)
c2 = range(1 ,10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('c2', hasattr(c2, '__iter__'))
print('c2', hasattr(c2, '__next__'))

for i in c1:
    if i > 100:
        break

    print(i)

for i in c2:
    print(i)
