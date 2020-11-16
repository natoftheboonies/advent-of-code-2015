samples = [r'"aaa\"aaa"',r'"\x27"',r'"abc"',r'""']

def cheater(string):
	return len(string)-len(eval(string))

assert sum([cheater(x) for x in samples]) == 12

def encoder(string):
	return 2+string.count('"')+string.count('\\')

assert sum([encoder(x) for x in samples]) == 19

with open('input8') as fp:
	samples = fp.readlines()

print('#1',sum([cheater(x.strip()) for x in samples]))
print('#2',sum([encoder(x.strip()) for x in samples]))
