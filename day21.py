weapons_in = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
""".splitlines()

armor_in = """Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
""".splitlines()

rings_in = """Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""".splitlines()

def parse(lines):
	parsed = []
	for x in lines[1:]:
		comp = x.split()
		cost, damage, armor = map(int,comp[-3:])
		label = ' '.join(comp[:-3])
		parsed.append((label,cost,damage,armor))

	return parsed

# label, cost, damage, armor
weapons = parse(weapons_in)
armors = parse(armor_in)
armors.append(('None',0,0,0))
rings = parse(rings_in)
#print(armor)


def fight(player, boss):
	while player[0] > 0 and boss[0] > 0:
		boss[0] -= player[1]-boss[2]
		#print('boss',boss[0])
		if boss[0] <= 0:
			break
		player[0] -= boss[1]-player[2]
		#print('player',player[0])
	return 'player' if player[0] > 0 else 'boss'

player = [8,5,5]
boss = [12,7,2]
assert fight(player,boss) == 'player'



# hp, damage, armor
boss = [100,8,2]


from itertools import combinations

mincost = 999
for w in weapons:
	for a in armors:
		for numring in range(3):
			for r in combinations(rings,numring):
				stuff = [w,a]+list(r)
				cost = sum([item[1] for item in stuff])
				damage = sum([item[2] for item in stuff])
				protect = sum([item[3] for item in stuff])
				if cost < mincost and fight([100,damage,protect],boss[:])=='player':
					mincost = cost
print('#1',mincost) 

maxcost = 0
for w in weapons:
	for a in armors:
		for numring in range(3):
			for r in combinations(rings,numring):
				stuff = [w,a]+list(r)
				cost = sum([item[1] for item in stuff])
				damage = sum([item[2] for item in stuff])
				protect = sum([item[3] for item in stuff])
				if cost >= maxcost and fight([100,damage,protect],boss[:])=='boss':
					maxcost = cost
print('#2',maxcost) # 146 too low
