from collections import defaultdict

sample = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
'''.splitlines()

bitmax = 65535+1


# https://stackoverflow.com/questions/11557241/python-sorting-a-dependency-list
def topological_sort(source):
	"""perform topo sort on elements.

	:arg source: list of ``(name, [list of dependancies])`` pairs
	:returns: list of names, with dependancies listed first
	"""
	pending = [(name, set(deps)) for name, deps in source] # copy deps so we can modify set in-place
	emitted = []
	while pending:
		next_pending = []
		next_emitted = []
		for entry in pending:
			name, deps = entry
			deps.difference_update(emitted) # remove deps we emitted last pass
			if deps: # still has deps? recheck during next pass
				next_pending.append(entry)
			else: # no more deps? time to emit
				print('emit',name,emitted)
				yield name
				emitted.append(name) # <-- not required, but helps preserve original ordering
				next_emitted.append(name) # remember what we emitted for difference_update() in next pass
		if not next_emitted: # all entries have unmet deps, one of two things is wrong...
			print(len(next_pending))
			raise ValueError("cyclic or missing dependancy detected: %r" % (next_pending,))
		pending = next_pending
		emitted = next_emitted


def finddeps(left):
	gate = left.split()
	#print(gate)
	if len(gate)==1:
		if gate[0].isnumeric():
			return []
		else:
			return gate[0]
	elif len(gate)==2:
		return gate[1]
	elif 'SHIFT' in gate[1]:
		return gate[0]
	else:
		return (gate[0],gate[2])


def circuit(insts):
	wires = defaultdict(int)
	# looks like sorted in reverse alpha
	# nope, need to topological sort
	# nope, let's abandon this and just find 'a'

	proc = [tuple([x.strip() for x in inst.strip().split('->')]) for inst in insts]
	blah = [(x[1],finddeps(x[0])) for x in proc]
	print(blah)

	for key in topological_sort(blah):
		#print(key)
		inst = [x for x in proc if x[1] == key][0]
		left, right = inst

		gate = left.split()
		if len(gate) == 1:
			if gate[0].isnumeric():
				wires[right] = int(gate[0])
			else:
				wires[right] = wires[gate[0]]
		elif len(gate)==2: #NOT
			wires[right] = ~wires[gate[1]]
		else:
			if gate[1] == 'AND':
				wires[right] = wires[gate[0]] & wires[gate[2]]
			elif gate[1] == 'OR':
				wires[right] = wires[gate[0]] | wires[gate[2]]
			elif gate[1] == 'LSHIFT':
				wires[right] = wires[gate[0]] << int(gate[2])
			elif gate[1] == 'RSHIFT':
				wires[right] = wires[gate[0]] >> int(gate[2])
			else:
				print("???",gate)
		if wires[right] < 0:
			wires[right] += bitmax
	return wires


def eval_wire(insts, start, bval=None):
	proc = dict([tuple(reversed([x.strip() for x in inst.strip().split('->')])) for inst in insts])
	#print(proc)
	if bval:
		proc['b'] = str(bval)
	found = dict()

	def get(blah):

		if blah.isnumeric():
			#print(blah)
			return int(blah)
		else:
			#print('get',blah)
			if blah in found:
				return found[blah]
			else:
				result = evalgate(proc[blah])
				found[blah] = result
				return result

	def evalgate(left):
		gate = left.split()
		if len(gate) == 1:
			return get(gate[0])
		elif len(gate)==2: #NOT
			result = ~get(gate[1])
			return result+bitmax if result < 0 else result
		else:
			if gate[1] == 'AND':
				return get(gate[0]) & get(gate[2])
			elif gate[1] == 'OR':
				return (get(gate[0])) | get(gate[2])
			elif gate[1] == 'LSHIFT':
				result = get(gate[0]) << get(gate[2])
				return result+bitmax if result < 0 else result
			elif gate[1] == 'RSHIFT':
				result = get(gate[0]) >> get(gate[2])
				return result+bitmax if result < 0 else result
			else:
				print("???",gate)

	return evalgate(proc[start])





#wires = circuit(sample)

assert eval_wire(sample,'d') == 72
assert eval_wire(sample,'i') == 65079

# for x in wires:
# 	print(x,wires[x])

with open('input7') as fp:
	insts = fp.readlines()

# for x in wires:
# 	print(x,wires[x])


print('#1',eval_wire(insts,'a'))
print('#2',eval_wire(insts,'a',eval_wire(insts,'a')))