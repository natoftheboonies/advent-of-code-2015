from itertools import count

def coords():
	for c in count(1):
		tmp = list(range(1,c))
		for pos in zip(tmp,reversed(tmp)):
			yield pos 

code = 20151125
mult = 252533
div = 33554393
n = 0
debug = False
for p in coords():
	if debug and n < 20:
		print(p,code)
		n+=1
	# goal = row 2947, column 3029
	if p == (3029, 2947):
		break
	code = code*mult%div
print('#1',code)