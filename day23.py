
def runprog(prog,reg={'a':0,'b':0}):

	ptr = 0

	while ptr < len(prog):
		#print(prog[ptr])
		inst = prog[ptr].split()
		cmd = inst[0]
		args = inst[1:]
		if cmd == 'hlf':
			reg[args[0]] //= 2
		elif cmd == 'tpl':
			reg[args[0]] *= 3
		elif cmd == 'inc':
			reg[args[0]] += 1
		elif cmd == 'jmp':
			ptr += int(args[0])
			continue
		elif cmd == 'jie':
			r = args[0].strip(',')
			if reg[r]%2==0:
				ptr += int(args[1])
				continue
		elif cmd == 'jio':
			r = args[0].strip(',')
			if reg[r]==1:
				ptr += int(args[1])
				continue
		else:
			print('unexpected cmd',cmd)

		ptr += 1
	return reg


sample = '''inc a
jio a, +2
tpl a
inc a
'''.splitlines()

prog = [line.strip() for line in sample]

with open('input23') as fp:
	lines = fp.readlines()

prog = [line.strip() for line in lines]

reg = runprog(prog)
print('#1',reg['b'])

reg = runprog(prog,{'a':1,'b':0})
print('#2',reg['b'])