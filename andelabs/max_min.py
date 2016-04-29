def find_max_min(num):
	h = min (num)
	m = max (num)
	
	if h == m:
	  return [len(num)]
	return [h, m]