
def nice(string):
	if any(n in string for n in ['ab','cd','pq','xy']):
		return False
	if sum([string.count(c) for c in 'aeiou']) < 3:
		return False
	nice = False
	for c in range(len(string)-1):
		if string[c]==string[c+1]:
			nice = True
	return nice

assert nice('ugknbfddgicrmopn')
assert nice('aaa')
assert not nice('jchzalrnumimnmhp')
assert not nice('haegwjzuvuyypxyu')
assert not nice('dvszwmarrgswjxmb')

with open('input5') as fp:
	strings = fp.readlines()

nice = len([string for string in strings if nice(string.strip())])
print('#1',nice)

def nice2(string):
	pair = repeat = False
	for c in range(len(string)-2):
		if string[c:c+2] in string[c+2:]:
			pair = True
		if string[c]==string[c+2]:
			repeat = True
	return pair and repeat

assert nice2('qjhvhtzxzqqjkmpb')
assert nice2('xxyxx')
assert not nice2('uurcxstgmygtbstg')
assert not nice2('ieodomkazucvgmuy')

nice2 = len([string for string in strings if nice2(string.strip())])
print('#2',nice2)