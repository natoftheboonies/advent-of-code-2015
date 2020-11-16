
from collections import defaultdict



def countlights(insts):
	lights = defaultdict(int)
	brights = defaultdict(int)
	for inst in insts:
		cmd = inst.strip().split()
		start = tuple(map(int,cmd[-3].split(',')))
		end = tuple(map(int,cmd[-1].split(',')))
		if cmd[0] == 'turn':
			if cmd[1] == 'on':
				for x in range(start[0],end[0]+1):
					for y in range(start[1],end[1]+1):
						lights[(x,y)]=1
						brights[(x,y)]+=1
			elif cmd[1]=='off':
				for x in range(start[0],end[0]+1):
					for y in range(start[1],end[1]+1):
						lights[(x,y)]=0
						if brights[(x,y)] > 0:
							brights[(x,y)]-=1
		elif cmd[0]=='toggle':
			for x in range(start[0],end[0]+1):
				for y in range(start[1],end[1]+1):
					lights[(x,y)]=(lights[(x,y)]+1)%2
					brights[(x,y)]+=2
	return sum(lights.values()),sum(brights.values())

sample = '''turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500
'''.splitlines()

with open('input6') as fp:
	lines = fp.readlines()

lights, brights = countlights(lines)

print('#1',lights)
print('#2',brights) #not 13396307
