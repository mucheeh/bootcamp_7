# x: 10, y: 20, z: 40
# x: 10, y: 40
# x: 4, y: 5, z: 50

f = [(10, 20, 40), (10, 40), (4, 5, 50)]

for itm in f:
	if len(itm) == 2:
		print "x: {}, y: {}".format(*itm)
	elif len(itm) == 3:
		print "x: {}, y: {}, z: {}".format(*itm)
	else:
		print "Not valid"
