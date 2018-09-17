
def fib(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		return fib(x - 1) + fib(x - 2)


fib_0 = fib(0)
assert fib_0 == 0, fib_0

fib_1 = fib(1)
assert fib_1 == 1, fib_1

fib_2 = fib(2)
assert fib_2 == 1, fib_2

fib_3 = fib(3)
assert fib_3 == 2, fib_3

fib_4 = fib(4)
assert fib_4 == 3, fib_4

fib_5 = fib(5)
assert fib_5 == 5, fib_5

fib_6 = fib(6)
assert fib_6 == 8, fib_6

fib_7 = fib(7)
assert fib_7 == 13, fib_7

print(fib_0)
print(fib_1)
print(fib_2)
print(fib_3)
print(fib_4)
print(fib_5)
print(fib_6)
print(fib_7)
