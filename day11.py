
#chr ord 97-123

def testpasswd(passwd):
	if any(c in passwd for c in ['i','o','l']):
		return False
	straight = pair = pair2 = False
	for c in range(len(passwd)-2):
		if ord(passwd[c])+1 == ord(passwd[c+1]) and ord(passwd[c+1])+1 == ord(passwd[c+2]):
			straight = True
		if not pair and passwd[c]==passwd[c+1]:
			pair = True
		if pair and c < len(passwd)-3 and passwd[c+2] == passwd[c+3]:
			pair2 = True
	return straight and pair and pair2

def nextpasswd(passwd):
	lpasswd = list(passwd)
	for c in range(len(passwd)-1,-1,-1):
		if ord(passwd[c])==122: # z
			lpasswd[c]='a'
		else:
			lpasswd[c]=chr(ord(lpasswd[c])+1)
			return ''.join(lpasswd)
	print('fail',lpasswd)
	return 'nat'

assert not testpasswd('hijklmmn')
assert not testpasswd('abbceffg')
assert not testpasswd('abbcegjk')
assert testpasswd('abcdffaa')
assert testpasswd('abbbcddk')
assert not testpasswd('abbbcdek')

assert nextpasswd('xx')=='xy'
assert nextpasswd('xz')=='ya'

def findnext(start):
	while not testpasswd(start):
		start = nextpasswd(start)
	return start

assert findnext('abcdefgh')=='abcdffaa'
#assert findnext('ghijklmn')=='ghjaabcc' # slow

passwd = 'hepxcrrq'
passwd = findnext(passwd)
print('#1',passwd)

passwd = findnext(nextpasswd(passwd))
print('#2',passwd)
