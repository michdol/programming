import unittest

from algorithm import quick_sort, partition, exchange, randomized_quick_sort, alternative_quick_sort


class QuickSortTest(unittest.TestCase):
	def test_exchange(self):
		array = [1, 2]
		exchange(array, 0, 1)
		self.assertEqual(array, [2, 1])

		array = [1, 2]
		exchange(array, 1, 0)
		self.assertEqual(array, [2, 1])

		array = [1, 2, 3, 4]
		exchange(array, 0, 3)
		self.assertEqual(array, [4, 2, 3, 1])

		array = [1, 2, 3, 4]
		exchange(array, 1, 3)
		self.assertEqual(array, [1, 4, 3, 2])

	def test_partition(self):
		array = [2, 8, 7, 1, 3, 5, 6, 4]
		partition(array, 0, len(array) - 1)
		#						          *
		self.assertEqual(array, [2, 1, 3, 4, 7, 5, 6, 8])

	def test_quick_sort(self):
		array = [2, 8, 7, 1, 3, 5, 6, 4]
		quick_sort(array, 0, len(array) - 1)
		self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8])

	def test_randomized_quick_sort(self):
		array = [2, 8, 7, 1, 3, 5, 6, 4]
		randomized_quick_sort(array, 0, len(array) - 1)
		self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8])

	def test_alternative_quick_sort(self):
		array = [2, 8, 7, 1, 3, 5, 6, 4]
		arr = alternative_quick_sort(array)
		self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8])

	def test_alternative_quick_sort_single_element(self):
		array = [2]
		arr = alternative_quick_sort(array)
		self.assertEqual(arr, [2])


if __name__ == "__main__":
	unittest.main()
