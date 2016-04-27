from person import Person
from kenyan import Kenyan

# ASIDE:
# Read about:
# PEP8
# Instance vs class variables vs.
# class methods (advanced topic)

# putting something into the object
p = Person('Joe', 23)
print p

p1 = Person('John', 24)
p2 = Person('Jane', 25)

# a is a tuple
a = [('Jane', 23), ('Joe', 50), ('Jackie', 34), ('Jacob', 23), ('Jee', 18), ('Josh', 60)]

# empty list
b = []

# creating an object
for name, age in a:
	person = Person(name, age)
	b.append(person)

k = Kenyan('Anita Waiguru',20)

k.probe(True)


# print p.say_hello(), p1.say_hello(), p2.say_hello()

# printing name and age
print p.name
print p.age
print Person.people_count
print p2.people_count
print b
print "Is {} corrupt? {}".format(k.name, k.is_corrupt())
print k.say_hello()