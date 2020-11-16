import re

with open ('input12') as fp:
	sample = fp.read().strip()

result = sum([int(x) for x in re.findall(r'-?\d+', sample)])

count = 0
for x in re.findall(r'-?\d+', sample):
	print(x)
	count += 1
	if count > 10:
		break

print('#1',result) # not 176852


def part2(foo):
	if isinstance(foo,int):
		return foo
	if isinstance(foo,dict):
		if "red" in foo.values():
			return 0
		else:
			here = 0
			for k, v in foo.items():
				here += part2(k)
				here += part2(v)
			return here
	elif isinstance(foo,list):
		here = 0
		for f in foo:
			here += part2(f)
		return here
	# elif foo.isnumeric():
	# 	return int(foo)
	return 0


import json
blah = json.loads(sample)

print('#2',part2(blah))