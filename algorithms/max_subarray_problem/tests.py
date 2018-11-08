from unittest import TestCase, main

from algorithm import find_max_crossing_subarray, find_max_subarray, find_max_subarray_brute_force, arr, long_arr


class MaxSubArrayProblemTest(TestCase):
	def test_find_max_crossing_subarray(self):
		low = 0
		high = len(arr)
		mid = high // 2
		result = find_max_crossing_subarray(arr, low, mid, high)
		self.assertEqual(result, (7, 10, 43))

	def test_find_max_subarray(self):
		low = 0
		high = len(arr) - 1
		result = find_max_subarray(arr, low, high)
		self.assertEqual(result, (7, 10, 43))

	def test_find_max_subarray_brute_force(self):
		low = 0
		high = len(arr) - 1
		result = find_max_subarray_brute_force(arr, low, high)
		self.assertEqual(result, (7, 10, 43))

	def test_find_max_subarray_long_arr(self):
		low = 0
		high = len(long_arr) - 1
		result = find_max_subarray(long_arr, low, high)
		self.assertEqual(result, (8, 45, 656))

	def test_find_max_subarray_brute_force_long_arr(self):
		low = 0
		high = len(long_arr) - 1
		result = find_max_subarray_brute_force(long_arr, low, high)
		self.assertEqual(result, (8, 45, 656))


if __name__ == "__main__":
	main()
