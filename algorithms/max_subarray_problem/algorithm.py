import timeit

_negative_infinity_ = -9999999999999999999999
										 #
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
long_arr = [
	20, -21, 43, -23, -92, 45, -56, -5, 34, -17, 34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49, 3, -45, 34, 76, 32,
	-76, -2, 3, -45, 44, 34, 67, -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34, 88, 56, -6, -89, -90, -34, -56, 23,
	29, 2, 6, 9, 2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55, 23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56, -34,
	45, 32, 20, -87, 39, 82, 95, -67, -45, 88, -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76
]


def find_max_crossing_subarray(array, low, mid, high):
	left_sum = _negative_infinity_
	sum_ = 0
	max_left = mid
	for i in range(mid, low, -1):
		sum_ = sum_ + array[i]
		if sum_ > left_sum:
			left_sum = sum_
			max_left = i

	right_sum = _negative_infinity_
	sum_ = 0
	max_right = mid + 1
	for j in range(mid + 1, high):
		sum_ = sum_ + array[j]
		if sum_ > right_sum:
			right_sum = sum_
			max_right = j
	return max_left, max_right, left_sum + right_sum


def find_max_subarray(array, low, high):
	if high == low:
		return low, high, array[low]
	else:
		mid = (low + high) // 2
		left_low, left_high, left_sum = find_max_subarray(array, low, mid)
		right_low, right_high, right_sum = find_max_subarray(array, mid + 1, high)
		cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return left_low, left_high, left_sum
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return right_low, right_high, right_sum
		else:
			return cross_low, cross_high, cross_sum


def find_max_subarray_brute_force(array, low, high):
	sum_ = _negative_infinity_
	left = low
	right = high
	for i in range(low, high):
		tmp_sum = 0
		for j in range(i, high):
			tmp_sum += array[j]
			if tmp_sum >= sum_:
				sum_ = tmp_sum
				left = i
				right = j
	return left, right, sum_


def _time_recursive(arr):
	def tmp():
		high = len(arr)
		find_max_subarray(long_arr, 0, high)
	return tmp


def _time_brute_force(arr):
	def tmp():
		high = len(arr)
		find_max_subarray(long_arr, 0, high)
	return tmp


def time_function(func):
	results = []
	for i in range(0, len(long_arr)):
		tmp_arr = long_arr[:i]
		TIMER = timeit.Timer(func(tmp_arr))
		ret = TIMER.timeit(10)
		results.append(str(ret) + "\n")
	with open("results_%s.txt" % func.__name__, "w") as f:
		f.writelines(results)


def print_results(func1, func2):
	f1 = open("results_%s.txt" % func1.__name__, "r")
	f2 = open("results_%s.txt" % func2.__name__, "r")
	end = [0, 0]
	try:
		asd = []
		for idx, vals in enumerate(zip(f1, f2)):
			a = None
			left_val = float(vals[0][:-1])
			right_val = float(vals[1][:-1])
			if left_val > right_val:
				a = (0, 1)
			else:
				a = (1, 0)
			print("{}\n{}\n{}, {}\n".format(left_val, right_val, a, idx))
			end[0] += a[0]
			end[1] += a[1]
			asd.append([a, idx])
		print(end)
		[print(z) for z in asd]
	except Exception as e:
		print(e)
	finally:
		f1.close()
		f2.close()


# time_function(_time_recursive)
# time_function(_time_brute_force)
# print_results(_time_brute_force, _time_recursive)
