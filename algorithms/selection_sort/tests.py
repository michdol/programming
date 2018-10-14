import unittest

from algorithm import selection_sort, book_selection_sort


class SelectionSortTest(unittest.TestCase):
	def test_sort(self):
		arr = [4, 2, 5, 7, 1, 6, 3]
		sorted_array = selection_sort(arr)
		self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 6, 7])

	def test_sort_book(self):
		arr = [4, 2, 6, 7, 1, 5, 3]
		sorted_array = book_selection_sort(arr)
		self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
	unittest.main()
