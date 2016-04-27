#printing a in reverse
a = [10, 40, -9, 45, 60, 89]
print a


for i in range(len(a) -1, -1, -1):
	print a[i]

# printing b as x, y	
b = [(2, 4), (5, 10), (6, 20), (50, 50)]
print b

for x,y in b:
	print "x: {}, y: {}".format(x,y)
	# print "x: %s, y: %s"% (x, y)


# x: 10, y: 20, z: 40
# x: 10, y: 40
# x: 4, y: 5, z: 50


f = [(10, 20, 40), (10, 40), (4, 5, 50)]

if f = len(3):
for x,y,z in f:
	print "x: {}, y: {}, z: {}".format(x, y, z)
else:
	for x,y in f:
		print "x: {}, y: {}, z: {}".format(x, y)