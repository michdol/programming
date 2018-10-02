import unittest

from algorithm import insertion_sort, descending_insertion_sort, linear_search


class InsertionSortTest(unittest.TestCase):
	def test_sort(self):
		arr = [4, 2, 5, 7, 1, 6, 3]
		sorted_array = insertion_sort(arr)
		self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 6, 7])

	def test_descending_insertion_sort(self):
		arr = [4, 2, 5, 7, 1, 6, 3]
		sorted_array = descending_insertion_sort(arr)
		self.assertEqual(sorted_array, [7, 6, 5, 4, 3, 2, 1])

	def test_linear_search(self):
		arr = [4, 2, 5, 7, 1, 6, 3]
		index = linear_search(arr, 3)
		self.assertEqual(index, 6)

	def test_linear_search_no_result(self):
		arr = [4, 2, 5, 7, 1, 6, 3]
		index = linear_search(arr, 8)
		self.assertIsNone(index)


if __name__ == "__main__":
	unittest.main()
