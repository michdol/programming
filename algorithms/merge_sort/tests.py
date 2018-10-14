import unittest

from algorithm import merge, merge_sort


class MergeSortTest(unittest.TestCase):
	def test_merge(self):
		arr = [2, 4, 5, 7, 1, 2, 3, 6]
		merge(arr, 0, 3, 7)
		self.assertEqual(arr, [1, 2, 2, 3, 4, 5, 6, 7])

	def test_merge_odd(self):
		arr = [2, 4, 5, 7, 1, 2, 3, 6, 8]
		merge(arr, 0, 3, 8)
		self.assertEqual(arr, [1, 2, 2, 3, 4, 5, 6, 7, 8])

	def test_merge_sort(self):
		arr = [8, 2, 6, 5, 1, 7, 4, 3, 6, 6, 8, 7]
		n = len(arr)
		merge_sort(arr, 0, n - 1)
		self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8, 8])


if __name__ == "__main__":
	unittest.main()
