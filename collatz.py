collatz = {}
count = 0
max_chain = 0

def collat(n):
	count = 0
	while n != 1 and n not in collatz:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		count += 1
		if n in collatz:
			count += collatz[n]
	return count

for x in xrange(1, 1000001):
	collatz[x] = collat(x)
	if collatz[x] > max_chain:
		max_value, max_chain = x, collatz[x]
print (max_value, max_chain)