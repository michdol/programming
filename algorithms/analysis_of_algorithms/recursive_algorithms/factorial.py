def factorial(x):
	if x < 1:
		return 1
	else:
		return x * factorial(x - 1)


factorial_0 = factorial(0)
assert factorial_0 == 1

factorial_1 = factorial(1)
assert factorial_1 == 1

factorial_2 = factorial(2)
assert factorial_2 == 2

factorial_3 = factorial(3)
assert factorial_3 == 6

factorial_5 = factorial(5)
assert factorial_5 == 120
