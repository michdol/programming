count = 0


def maccarthy(x):
	global count
	count += 1
	if x > 100:
		return x - 10
	else:
		return maccarthy(maccarthy(x + 11))


# print(maccarthy(100))
print(count)
