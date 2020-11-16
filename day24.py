from itertools import combinations
from functools import reduce
from operator import mul

sample =  list(range(1,6))+list(range(7,12))

with open('input24') as fp:
	lines = fp.readlines()
sample = list(map(int,[line.strip() for line in lines]))

assert len(sample) == len(set(sample))
sample = set(sample)

groupsize = sum(sample)//3

found = False
min_qe = None
for size in range(1,len(sample)//2+1):
	for combo in combinations(sample,size):
		if sum(combo)==groupsize:
			qe = reduce(mul,combo)
			found = True
			if not min_qe or qe < min_qe:
				min_qe = qe
	if found:
		break

print('#1',min_qe)

groupsize = sum(sample)//4

found = False
min_qe = None
for size in range(1,len(sample)//2+1):
	for combo in combinations(sample,size):
		if sum(combo)==groupsize:
			qe = reduce(mul,combo)
			found = True
			if not min_qe or qe < min_qe:
				min_qe = qe
	if found:
		break

print('#2',min_qe)