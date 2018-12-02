from unittest import TestCase, main

from algorithm import counting_sort


class CountingSortTest(TestCase):
	def test_test(self):
		array = [2, 5, 3, 0, 2, 3, 0, 3]
		auxiliary_array = []
		counting_sort(array, auxiliary_array)


if __name__ == "__main__":
	main()
