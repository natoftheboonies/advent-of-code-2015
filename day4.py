from hashlib import md5
from itertools import count

key = 'yzbqklnj'

for i in count():
	if md5((key+str(i)).encode()).hexdigest().startswith('00000'):
		print('#1',i)
		break

for i in count():
	if md5((key+str(i)).encode()).hexdigest().startswith('000000'):
		print('#2',i)
		break