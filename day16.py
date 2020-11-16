ticker = {'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}

with open('input16') as fp:
	possible = fp.readlines()

darealsue = None

for line in possible:
	c = line.index(':')
	sue = int(line[:c].split()[1])
	props = dict([p.split(': ') for p in line[c+2:].strip().split(', ')])
	realsue = True
	for p in props:
		props[p] = int(props[p])
		if p in ['cats','trees']:
			if ticker[p] >= props[p]:
				realsue = False
		elif p in ['pomeranians','goldfish']:
			if ticker[p] <= props[p]:
				realsue = False
		else:
			if ticker[p] != props[p]:
				realsue = False
	if realsue:
		darealsue = sue
	if all(ticker[p] == props[p] for p in props):
		print('#1',sue)

print('#2',darealsue)

