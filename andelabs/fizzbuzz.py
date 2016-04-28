def fizzbuzz_(x):
	if x % 3 ==0 and x % 5 == 0:
		return "FizzBuzz"
	elif x % 3 == 0:
		return "Fizz"
	elif x % 5 == 0:
		return "Buzz"
	else:
		return x


print fizzbuzz_(3)
print fizzbuzz_(5)
print fizzbuzz_(15)
print fizzbuzz_(1)