sample = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
""".splitlines()

def parsedeers(sample):
	deers = []
	for line in sample:
		deer = line.strip().split()
		name = deer[0]
		speed = int(deer[3])
		duration = int(deer[6])
		rest = int(deer[-2])
		deers.append((name,speed,duration,rest))
	return deers

deers = parsedeers(sample)

def race(deers,time):
	maxdist = 0
	for name,speed,duration,rest in deers:
		dist = 0
		cycle = duration+rest
		cycles = time//cycle
		remainder = time%cycle
		dist += speed*duration*cycles
		dist += speed*min(duration,remainder)
		#print(name, dist)
		if dist > maxdist:
			maxdist = dist
	return maxdist

assert race(deers,1000)==1120

def score(deers,time):
	scores = {x[0]:0 for x in deers}
	dist = {x[0]:0 for x in deers}
	states = {x[0]:(True,1) for x in deers}
	for s in range(time):
		for name,speed,duration,rest in deers:
			flying, since = states[name]
			if flying:
				dist[name]+=speed
				if since == duration:
					states[name] = (not flying, 1)
					#print(name,'resting after',s)
				else:
					states[name] = (flying, since+1)
			if not flying:
				if since == rest:
					states[name] = (not flying, 1)
					#print(name,'flying after',s)
				else:
					states[name] = (flying, since+1)
		# score
		win = max(dist.values())
		for name,speed,duration,rest in deers:
			if dist[name] == win:
				scores[name]+=1
	#print(scores)
	return max(scores.values())

assert score(deers,1000)==689

with open('input14') as fp:
	sample = fp.readlines()

deers = parsedeers(sample)
print('#1',race(deers,2503))
print('#2',score(deers,2503))