
number = 30
best_case = [30, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
avg_case = [1, 1, 1, 1, 1, 1, 30, 1, 1, 1, 1, 1, 1]
worst_case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30]
no_match_case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

count = 0


def find_x(array, x):
	global count
	count += 1
	if not array:
		return False
	if array[0] == x:
		return True
	return find_x(array[1:], x)


if __name__ == "__main__":
	print(find_x(best_case, number))
	print(count)
	count = 0
	print(find_x(avg_case, number))
	print(count)
	count = 0
	print(find_x(worst_case, number))
	print(count)
	count = 0
	print(find_x(no_match_case, number))
	print(count)
