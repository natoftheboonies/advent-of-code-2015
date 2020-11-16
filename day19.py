sample = """H => HO
H => OH
O => HH

HOH
""".splitlines()

def parse(lines):
	replace = set()
	mol = None
	for line in lines:
		if not line:
			continue
		if "=>" in line:
			a,b = line.strip().split(" => ")
			replace.add((a,b))
		else:
			mol = line.strip()

	return mol,replace

def part1(mol, replace):
	unique = set()
	for a,b in replace:
		start = 0
		while a in mol[start:]:
			start = mol.index(a,start)
			unique.add(mol[:start]+b+mol[start+len(a):])
			start += len(a)
	return len(unique)

assert part1(*parse(sample))==4


# let's try to go from mol back to 'e'

sample = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".splitlines()


def part2(mol, replace):
	def shrink(mol,depth):
		if mol == 'e':
			print('won at depth',depth)
			return depth
		depths = set()
		for a,b in replace:
			start = 0
			while b in mol[start:]:
				start = mol.index(b,start)
				mol_next = mol[:start]+a+mol[start+len(b):]
				depths.add(shrink(mol_next,depth+1))
				start += len(b)
		if depths:
			return min(depths)
		return 999

	return shrink(mol,0)

_, replace = parse(sample)

assert part2('HOH',replace) == 3
#assert part2('HOHOHO',replace) == 6

with open('input19') as fp:
	lines = fp.readlines()

mol, replace = parse(lines)

print('#1',part1(mol,replace)) # 615 too high


#print('#2',part2(mol,replace))
# works, but runs forever

# simplified https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4puwb/
# shouldn't work, but does?!
part2 = 0
while mol != 'e':
	for a, b in replace:
		if b not in mol:
			continue
		mol = mol.replace(b, a, 1)
		part2 += 1

print('#2',part2)
