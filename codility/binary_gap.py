def solution(N):
	max_ = 0
	current = 0

	#skip the tailing zero(s)
	while a > 0 and a%2 == 0:
		a //= 2

	while a > 0:
		rem = a%2
		if rem == 0:

			current += 1
		else:

			if current != 0:
				max_ = max(current, max_)
				current = 0
		a //= 2

	return max_

