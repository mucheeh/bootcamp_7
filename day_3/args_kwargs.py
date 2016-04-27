#Unpacking
def hello(name, age):
	'''
	Explains what it does..
	'''

	return "I am {}, and I'm {} years old".format(name, age)

people = [
			("Jane", 23),
			("Joe", 25),
			("Brian", 60),
			("Betty", 25)
		]

# for name, age in people:
# 	print hello(name, age)

for person in people:
	# print hello(person[0], person[1])
	print hello(*person)


def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10, 20) = 30
	super_sum(10, 20, 40) = 70
	super_sum(1, 4, 5, 6, 7) = 23
	'''

	total = 0
	for i in args:
		total += i

	return total
print super_sum(10, 20)
print super_sum(10, 20, 40)
print super_sum(1, 4, 5, 6, 7)

# unpacks then adds
a = [10, 40, 60]
print super_sum(*a)


b = [10, 20]
print super_sum(*b)

c = [10, 20, 30]
print super_sum(*c)

d = [1, 4, 5, 6, 7]
print super_sum(*d)

# kwargs
# can use back slash to start another line and continue with a one line code
def hello_again(**kwargs):
	return "I am {}, and I'm {}".format(kwargs['name'], kwargs['age'])
print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')


# list of dictionaries
other_people = [
		{'name': 'Joe', 'age': 98},
		{'name': 'Jane', 'age': 60},
		{'name': 'Trump', 'age': 23}
	]

joe = {'name': 'Joe', 'age': 98}
print hello_again(**joe)

for person in other_people:
	hello_again(**person)