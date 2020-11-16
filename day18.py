


def build_display(lines,part2=False):
	display = dict()
	for y, line in enumerate(lines):
		for x, light in enumerate(line.strip()):
			display[(x,y)] = light
	if part2:
		x,y = max(display)
		for pos in [(0,0),(x,0),(0,y),(x,y)]:
			display[pos] = '#'
	return display

def show(display):
	x,y = max(display)
	for y in range(y+1):
		for x in range(x+1):
			print(display[x,y],end='')
		print()
	print()

def animate(display,part2):
	display_new = dict(display)
	for pos in display:
		dirs = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1),(-1,1)]
		neighbors_on = [display.get((pos[0]+x,pos[1]+y),'.') for (x,y) in dirs].count('#')
		if display[pos] == '#':
			if neighbors_on < 2 or neighbors_on > 3:
				display_new[pos] = '.'
		else: # display[pos] == '.'
			if neighbors_on == 3:
				display_new[pos] = '#'
	if part2:
		x,y = max(display_new)
		for pos in [(0,0),(x,0),(0,y),(x,y)]:
			display_new[pos] = '#'
	return display_new


def cycle(display,times,part2=False):
	for _ in range(times):
		display = animate(display,part2)
	return display

sample = """.#.#.#
...##.
#....#
..#...
#.#..#
####..
""".splitlines()

assert list(cycle(build_display(sample),4).values()).count('#') == 4

assert list(cycle(build_display(sample,True),5,True).values()).count('#') == 17

with open('input18') as fp:
	lines = fp.readlines()

print('#1',list(cycle(build_display(lines),100).values()).count('#'))
print('#2',list(cycle(build_display(lines,True),100,True).values()).count('#'))

