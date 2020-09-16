
# higher order functions
from functools import reduce
from operator import mul

b = lambda x: -x[0]
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=b)
print(pairs)

a = list(range(1, 10, 2))
print(a)

b = [x for x in a if x > 3]
print(b)

c = filter(lambda x: x > 3, a)
print(list(c))


def f(x):
    return 3 < x < 9


d = filter(f, a)
print(list(d))
print(len(a))

e = list(range(10000000))
r = True
for i in e:
    if i != e[0]:
        r = False
        # break
print(r)

r = all(x == e[0] for x in e)
print(r)

r = any(x == 1.5 for x in e)
print(r)

evens = list(map(lambda n: n*2, range(20)))
print(evens)

a = range(1, 10)
b = reduce(mul, a)
print(b)


# median - the value separates the higher half from the lower half
nums = [16, 3, 2, 4, 11, 1, 12, 8, 9, 7, 10, 13, 15, 17]
import statistics
print(statistics.median(nums))


# manual way
def median(nums):
    s = sorted(nums)
    half_way = len(nums) // 2 - 1  # because index is 0 based
    if len(nums) % 2 == 0:  # even
        return (s[half_way] + s[half_way + 1]) / 2
    else:
        return s[half_way + 1]


print(median(nums))
print(median([1, 2, 3, 4, 5]))  # 3
print(median([1, 2, 3, 4]))  # 2.5
