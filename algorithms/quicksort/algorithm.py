import pdb


def quick_sort(array, p, r):
	if p < r:
		q = partition(array, p, r)
		quick_sort(array, p, q - 1)
		quick_sort(array, q + 1, r)


def exchange(array, i, j):
	first = array[i]
	second = array[j]
	array[i] = second
	array[j] = first


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
