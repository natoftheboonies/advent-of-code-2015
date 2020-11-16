from itertools import combinations
from functools import reduce
from operator import mul

def wrap(package):
	sides = [x*y for x,y in combinations(map(int,package.split('x')),2)]
	return sum([2*x for x in sides]+[min(sides)])

assert wrap("2x3x4") == 58
assert wrap("1x1x10") == 43

with open('input2') as fp:
	packages = fp.readlines()

print('#1',sum([wrap(pkg.strip()) for pkg in packages]))

def tie(package):
	dims = sorted(map(int,package.split('x')))
	around = sum([2*d for d in dims[:-1]])
	bow = reduce(mul,dims)
	return around+bow

assert tie("2x3x4") == 34
assert tie("1x1x10") == 14

print('#2',sum([tie(pkg.strip()) for pkg in packages]))