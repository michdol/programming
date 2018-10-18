import unittest

from ddt import ddt, data

from algorithm import binary_search


@ddt
class BinarySearchTest(unittest.TestCase):
	def setUp(self):
		self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	@data(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
	def test_search(self, num):
		result = binary_search(self.arr, 0, len(self.arr) - 1, num)
		self.assertEqual(result, self.arr.index(num))

	def test_not_found(self):
		result = binary_search(self.arr, 0, len(self.arr) - 1, 11)
		self.assertEqual(result, -1)
		result = binary_search([], 0, 0 - 1, 1)
		self.assertEqual(result, -1)


if __name__ == "__main__":
	unittest.main()
