spells_in = """

    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns.
    	While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns.
    	At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
    	At the start of each turn while it is active, it gives you 101 new mana.
"""

# spell = cost, duration, effect
# effect = damage, heal, armor, mana

spells = [
{'spell':'Magic Missle', 'cost':53, 'duration':0, 'effect':
	{'damage':4,'heal':0, 'armor':0, 'mana':0}
},
{'spell':'Drain', 'cost':73, 'duration':0, 'effect':
	{ 'damage':2,'heal':2, 'armor':0, 'mana':0 }
},
{'spell':'Shield', 'cost':113, 'duration':6, 'effect':
	{ 'damage':0,'heal':0, 'armor':7, 'mana':0 }
},
{'spell':'Poison', 'cost':173, 'duration':6, 'effect':
	{ 'damage':3,'heal':0, 'armor':0, 'mana':0 }
},
{'spell':'Recharge', 'cost':229, 'duration':5, 'effect':
	{ 'damage':0,'heal':0, 'armor':0, 'mana':101 }
}]

debug = False


def play(player, boss, spells_active, spell=None,part2=False):
	# player turn: apply spells, cast spell
	# boss turn: apply spells, deal damage
	if debug:
		if spell:
			print('-- Player turn --')
		else:
			print('-- Boss turn --')
		print('- Player has',player[1],'hit points,',player[0],'mana')
		print('- Boss has',boss[1],'hit points')

	# apply spells
	armor = 0
	for s in spells_active:
		s[0]-=1
		e = s[1]['effect']
		boss[1]-=e['damage']
		player[1]+=e['heal']
		player[0]+=e['mana']
		armor+=e['armor']
		if debug:
			print(s[1]['spell'],'deals stuff; timer is now',s[0])
	spells_active = [s for s in spells_active if s[0] > 0]

	if boss[1]<=0:
		if debug:
			print('Boss killed')
		return player, boss, spells_active

	if spell: # player turn

		# hard mode
		if part2:
			player[1]-=1
			if player[1] <= 0:
				return player, boss, spells_active

		if spell['duration'] > 0:
			spells_active.append([spell['duration'],spell])
		else:
			e = spell['effect']
			boss[1]-=e['damage']
			player[1]+=e['heal']
		player[0]-=spell['cost']
		if debug:
			print('Player cast',spell['spell'])


	else: # boss turn
		if debug:
			print('Boss attacks for',boss[2]-armor,'damage.')
		player[1]-=(boss[2]-armor)

	if debug:
		print()

	return player, boss, spells_active

def winner(player, boss):
	if player[1] <= 0 or boss[1] <= 0:
		# game over
		winner = player if player[1] > 0 else boss
		if len(winner) == 4:
			pass
			#print('player wins')
		else:
			pass
			#print('boss wins')
		return winner
	return None


def playstrategy(player, boss, strategy):
	cast = []
	pos = 0
	while player[1] > 0 and boss[1] > 0 and pos < len(strategy):

		# player turn
		spell = spells[strategy[pos]]
		pos += 1
		player, boss, cast = play(player,boss,cast,spell=spell)
		won = winner(player,boss)
		if won:
			return won

		# boss turn
		player, boss, cast = play(player,boss,cast)
		won = winner(player,boss)
		if won:
			return won

	return player, boss, cast

def sample1():

	#start
	#mana, hp, damage, armor
	player = [250,10,None,0]
	boss = [None,13,8]
	strategy = [3,0]

	return playstrategy(player, boss, strategy)


def sample2():

	#round 2:
	player = [250,10,None,0]
	boss = [None,14,8]
	strategy = [4,2,1,3,0]

	return playstrategy(player, boss, strategy)

sample1()
sample2()

def part1(part2=False):
	boss = [None,71,10]
	player = [500,50,None,0]
	spells_active = []

	spent = 0
	strategy = []
	won = None
	while not won:
		# player turn, pick a spell
		can_cast = [s for s in spells if s['cost'] <= player[0] and s not in [a for d,a in spells_active if d > 1]]
		if not can_cast:
			#print('no money left')
			return boss, strategy
		choice = can_cast[random.randrange(len(can_cast))]
		strategy.append(choice['spell'])
		spent += choice['cost']
		player, boss, spells_active = play(player,boss,spells_active,spell=choice,part2=part2)
		won = winner(player,boss)
		if won:
			return won, strategy, spent
		# boss turn
		player, boss, spells_active = play(player,boss,spells_active,part2=part2)
		won = winner(player,boss)
		if won:
			return won, strategy, spent


from collections import deque

def part1search(part2=False):
	boss = [None,71,10]
	player = [500,50,None,0]
	spells_active = []
	strategy = []
	spent = 0

	queue = deque()

	state = (spent, strategy, boss, player, spells_active)
	queue.append(state)
	count = 0

	mincost = 999999

	while queue:
		count += 1

			#print(queue)
		#print('loop')
		state = queue.popleft()
		spent, strategy, boss, player, spells_active = state
		if spent >= mincost:
			continue

		# player turn, pick a spell
		can_cast = [s for s in spells if s['cost'] <= player[0] and s not in [a for d,a in spells_active if d > 1]]
		if not can_cast:
			#print('no money left')
			continue
		for choice in can_cast:
			spent, strategy, boss, player, spells_active = state
			# the last bug, deep copy spells_active
			spells_active = [s[:] for s in spells_active]
			strategy = list(strategy)
			strategy.append(choice['spell'])
			spent += choice['cost']
			player, boss, spells_active = play(player[:],boss[:],spells_active[:],spell=choice,part2=part2)
			won = winner(player,boss)
			if won:
				if len(won)==4:
					if spent < mincost:
						mincost = spent
					#print('player won:',spent)
				else:
					#print('boss won 1')
					pass
				continue
				#return won, strategy, spent
			# boss turn
			player, boss, spells_active = play(player[:],boss[:],spells_active[:],part2=part2)
			won = winner(player,boss)
			if won:
				if len(won)==4:
					if spent < mincost:
						mincost = spent
						# if part2:
						# 	print(strategy)
					#print('player won:',spent)
				else:
					pass
					#print(strategy)
					#print('boss won 2')
				continue
			else:
				state2 = (spent, strategy,boss,player,spells_active)
				queue.append(state2)
	return mincost
	print('mincost',mincost)

print('#1',part1search())
print('#2',part1search(True))

import random

def part1loop():
	mincost = 9999
	for x in range(1000000):
		result = part1()
		if len(result[0])==4 and result[2] < mincost:
			mincost = result[2]
			print(result[2],result[1])
	print('#1',mincost) # 1824

#part1loop()


def part2loop():
	mincost = 9999
	for x in range(1000000):
		result = part1(part2=True)
		if len(result[0])==4 and result[2] < mincost:
			mincost = result[2]
			print(result[2],result[1])
	print('#1',mincost) # 1824

#part1loop()
# need a proper search instead of random spam for pt2
