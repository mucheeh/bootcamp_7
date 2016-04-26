def sum_digits(A):
	'''
	Takes a list A, and returns
	the sum of all the digits in the list
	e.g. [10,30, 45] should return 
	1 + 0 + 3 + 0 + 4 + 5 
	'''
	total = 0

	h = [10, 30, 45]

	for x in A:
		m = str(x)
		for k in m:
			p = int(k)
			total += p

	return total
print sum_digits([10, 30, 45])

