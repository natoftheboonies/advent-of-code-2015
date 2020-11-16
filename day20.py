from collections import defaultdict

def get_factors(n):
    x = 1
    factors = []
    while x ** 2 <= n:
        if n % x == 0:
            factors.append(x)
            factors.append(n // x)
        x += 1
    return factors


goal = 34000000

house = defaultdict(int)

for i in range(1,goal//10):
    for j in range(i,goal//10,i):
        house[j] += i * 10
print('#1',min([x for x in house if house[x] > goal])) # 786240

house = defaultdict(int)
for i in range(1,goal//10):
    for j in range(i,min(i*50,goal//10),i):
        house[j] += i * 11
print('#2',min([x for x in house if house[x] > goal])) # 786240
