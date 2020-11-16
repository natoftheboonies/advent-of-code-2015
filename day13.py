from itertools import permutations

sample = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
""".splitlines()

with open('input13') as fp:
	sample = fp.readlines()

nodes = set()
edges = dict()

for line in sample:
	words = line.strip().split()
	person = words[0]
	person2 = words[-1][:-1]
	nodes.add(person)
	nodes.add(person2)
	cost = int(words[3])
	if words[2] == 'lose':
		cost *= -1

	edges[(person, person2)] = cost
	#edges[(person2, person)] = cost

#print (nodes)
#print (edges)

happiest = 0
for table in permutations(nodes):
	happy = 0
	for pos in range(len(table)-1):
		happy += edges[(table[pos],table[pos+1])]
		happy += edges[(table[pos+1],table[pos])]
	happy += edges[(table[0],table[-1])]
	happy += edges[(table[-1],table[0])]
	if happy > happiest:
		happiest = happy

print('#1',happiest)

nodes.add('me')

happiest = 0
for table in permutations(nodes):
	happy = 0
	for pos in range(len(table)-1):
		if 'me' in table[pos:pos+2]:
			continue
		happy += edges[(table[pos],table[pos+1])]
		happy += edges[(table[pos+1],table[pos])]
	if not (table[0]=='me' or table[-1] == 'me'):
		happy += edges[(table[0],table[-1])]
		happy += edges[(table[-1],table[0])]
	if happy > happiest:
		happiest = happy

print('#2',happiest)