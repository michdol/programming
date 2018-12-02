import pdb
from random import randrange
from time import sleep
from timeit import timeit


def quick_sort(array, p, r):
	if p < r:
		q = partition(array, p, r)
		quick_sort(array, p, q - 1)
		quick_sort(array, q + 1, r)


def randomized_quick_sort(array, p, r):
	if p < r:
		q = randomized_partition(array, p, r)
		randomized_quick_sort(array, p, q - 1)
		randomized_quick_sort(array, q + 1, r)


def exchange(array, i, j):
	first = array[i]
	second = array[j]
	array[i] = second
	array[j] = first


def randomized_partition(array, p, r):
	i = randrange(p, r)
	exchange(array, i, r)
	return partition(array, p, r)


def partition(array, p, r):
	x = array[r]
	i = p - 1
	for j in range(p, r):
		if array[j] <= x:
			i += 1
			exchange(array, i, j)
	exchange(array, i + 1, r)
	return i + 1


def alternative_quick_sort(array):
	less = []
	equal = []
	greater = []

	if len(array) > 1:
		pivot = array[0]
		for i in array:
			if i < pivot:
				less.append(i)
			elif i == pivot:
				equal.append(i)
			else:
				greater.append(i)
		return alternative_quick_sort(less) + equal + alternative_quick_sort(greater)
	else:
		return array


def test_performance():
	number = 1000
	setup_quick_sort = "arr = [2, 8, 7, 1, 3, 5, 6, 4]; from __main__ import quick_sort"
	quick_sort_result = timeit(
		"quick_sort(arr, 0, 7)",
		number=number,
		setup=setup_quick_sort
	)
	sleep(1)

	setup_randomized_quick_sort = "arr = [2, 8, 7, 1, 3, 5, 6, 4]; from __main__ import randomized_quick_sort"
	randomized_quick_sort_result = timeit(
		"randomized_quick_sort(arr, 0, 7)",
		number=number,
		setup=setup_randomized_quick_sort
	)
	sleep(1)

	setup_alternative_quick_sort = "arr = [2, 8, 7, 1, 3, 5, 6, 4]; from __main__ import alternative_quick_sort"
	alternative_quick_sort_result = timeit(
		"alternative_quick_sort(arr)",
		number=number,
		setup=setup_alternative_quick_sort
	)

	print(quick_sort_result, "\t\tquick_sort_result")
	print(randomized_quick_sort_result, "\trandomized_quick_sort_result")
	print(alternative_quick_sort_result, "\talternative_quick_sort_result")
	print("\nquick_sort_result / randomized_quick_sort_result")
	print(quick_sort_result / randomized_quick_sort_result)
	print("\nquick_sort_result / alternative_quick_sort_result")
	print(quick_sort_result / alternative_quick_sort_result)
	print("\nrandomized_quick_sort_result / alternative_quick_sort_result")
	print(randomized_quick_sort_result / alternative_quick_sort_result)


if __name__ == "__main__":
	test_performance()
