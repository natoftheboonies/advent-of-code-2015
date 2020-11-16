
sample = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
""".splitlines()


# b + c = 100
# cap = -1*b+2*c
# dur = -2*b+3*c
# fla = 6*b+-2*c
# tex = 3*b+-1*c
# cal = 8*b+3*c

# simplex method looks hard.

# tasty = (-1*b+2*c)*(-2*b+3*c)*(6*b+-2*c)*(3*b+-1*c)
# tasty = (-1*b+2*(100-b))*(-2*b+3*(100-b))*(6*b+-2*(100-b))*(3*b+-1*(100-b))
# tasty = (-1*b+200-2b)*(-2*b+300-3b)*(6*b-200+2b)*(3*b+-100+b)
# tasty = (200-3b)*(300-5b)*(8b-200)*(4b-100)

maxb = 0
select = None
for b in range(1,101):
	cap = max(0,-1*b+2*(100-b))
	fla = max(0,-2*b+3*(100-b))
	tex = max(0,6*b-2*(100-b))
	cal = max(0,3*b+-1*(100-b))
	thisb = cap*fla*tex*cal
	if thisb > maxb:
		select = b
		maxb = thisb

#print(select)


real = """Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
""".splitlines()

maxscore = 0
select = None
max500 = 0
select500 = None

for su in range(0,101):
	for sp in range(0,101-su):
		for ca in range(0,101-su-sp):
			ch = 100-su-sp-ca
			# if su+sp+ca > 100:
			# 	continue
			cap = 3*su-3*sp-1*ca
			if cap <= 0:
				continue
			dur = 3*sp
			if dur <= 0:
				continue
			fla = 4*ca-2*ch
			if fla <= 0:
				continue
			tex = -3*su+2*ch
			if tex <= 0:
				continue
			score = cap*dur*fla*tex
			if score > maxscore:
				select = (su, sp, ca, ch)
				maxscore = score
			cal = 2*su+9*sp+1*ca+8*ch
			if cal == 500:
				if score > max500:
					select500 = (su, sp, ca, ch)
					max500 = score

print('#1',maxscore,select)
print('#2',max500,select500)

