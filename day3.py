

def follow(path):
	visited = set()
	pos = complex(0)
	visited.add(pos)
	for d in path:
		if d == '^':
			pos += 1j
		elif d == '>':
			pos += 1
		elif d == 'v':
			pos -= 1j
		elif d == '<':
			pos -= 1
		else:
			print('unexpected',d)
		visited.add(pos)
	return len(visited)


assert follow('^>v<')==4
assert follow('>')==2
assert follow('^v^v^v^v^v')==2

with open('input3') as fp:
	path = fp.read().strip()

print('#1',follow(path))

def robofollow(path):
	visited = set()
	santa = robo = complex(0)
	visited.add(santa)
	count = 0
	for d in path:
		pos = santa if count%2==0 else robo
		if d == '^':
			pos += 1j
		elif d == '>':
			pos += 1
		elif d == 'v':
			pos -= 1j
		elif d == '<':
			pos -= 1
		else:
			print('unexpected',d)
		visited.add(pos)
		if count%2==0:
			santa = pos
		else:
			robo = pos
		count += 1
	return len(visited)

assert robofollow('^v')==3
assert robofollow('^>v<')==3
assert robofollow('^v^v^v^v^v')==11

print('#2',robofollow(path))