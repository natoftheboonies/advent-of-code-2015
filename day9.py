
from itertools import permutations
sample = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
""".splitlines()

with open('input9') as fp:
	sample = fp.readlines()

nodes = set()
edges = dict()

for line in sample:
	left, right = line.split(" = ")
	city, city2 = left.split(" to ")
	nodes.add(city)
	nodes.add(city2)
	edges[(city, city2)] = int(right)
	edges[(city2, city)] = int(right)

cheap = 9999
teuer = 0
for route in permutations(nodes):
	cost = 0
	for c in range(len(route)-1):
		cost += edges[(route[c],route[c+1])]
	if cost < cheap:
		cheap = cost
	if cost > teuer:
		teuer = cost
print('#1',cheap)
print('#2',teuer)
