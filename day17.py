from itertools import combinations

def bins(sample,target,begin=2):
	min_bins = False
	min_combos = 0
	count = 0
	for x in range(begin,len(sample)):
		for c in combinations(sample,x):
			if sum(c)==target:
				count += 1
				if not min_bins and not min_combos:
					min_bins = True
				if min_bins:
					min_combos += 1
		min_bins = False
	return count, min_combos

sample = [20, 15, 10, 5, 5]
print('#sample',bins(sample,25,2))

with open('input17') as fp:
	sample = list(map(int,[x.strip() for x in fp.readlines()]))

print('#1,#2',bins(sample,150,3))
