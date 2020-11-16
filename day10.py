
start = '1'

def looksay(start,count):
	for _ in range(count):
		result = ''
		c = 0
		while c < len(start):
			dig = start[c]
			count = 1
			while c < len(start)-1 and start[c+1]==dig:
				count += 1
				c+=1
			result+=str(count)+str(dig)
			c += 1
		start = result
	return result

assert looksay('1',5)=='312211'

puzzle = '1113222113'
print('#1',len(looksay(puzzle,40)))

print('#2',len(looksay(puzzle,50)))