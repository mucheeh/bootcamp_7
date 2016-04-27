def data_type(x):
	'''
	Takes in an argument, x:
		-For an integer, return x** 2
		-For a float, return x / 2
		-For a string, returns "hello" + x
		-For a boolean, return "boolean"
		-For a long, return square root of x
	'''

	if type(x) == int:
		return x**2
	elif type(x) == float:
		return x/2
	elif type(x) == str:
		return "Hello {}".format(x)
	elif type(x) == bool:
		return "boolean"
	elif type(x) == long:
		return "long"
	else:
		return "invalid"

print data_type(1)
print data_type(1.65)
print data_type("hellen")
print data_type(True)
print data_type(50 ** 50)
