#printing a in reverse
a = [10, 40, -9, 45, 60, 89]
print a


for i in range(len(a) -1, -1, -1):
	print a[i]

# printing b as x, y	
b = [(2, 4), (5, 10), (6, 20), (50, 50)]
print b

for x, y in b:
	print "x: {}, y: {}".format(x,y)
	# print "x: %s, y: %s"% (x, y)



