import unittest

from algorithm import heap_sort


class InsertionSortTest(unittest.TestCase):
	def test_sort(self):
		heap_sort()


if __name__ == "__main__":
	unittest.main()
