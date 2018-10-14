import pdb

"""
Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the
element in A[1].
Then find the second smallest element of A, and exchange it with A[2].
Continue in this manner for the first n - 1 elements of A.

- Write pseudocode for this algorithm, which is known as selection sort.
- What loop invariant does this algorithm maintain?
- Why does it need to run for only the first n - 1 elements, rather than for all n elements?
- Give the best-case and worst-case running times of selection sort in ‚Theta-notation.
"""


def selection_sort(arr):
	# Iterate over n - 1 elements of the array.

	# In first iteration find smallest element of the array.
	# Exchange it with element in first position of the array.

	# In second iteration find smallest element of the array[1:].
	# Exchange it with the element in second position of the array.

	# Continue until reaching WHAT? n - 1
	length = len(arr)
	length_minus_one = length - 1
	i = 0
	while i < length_minus_one:
		smallest = i
		for j in range(i + 1, length):
			if arr[j] < arr[smallest]:
				smallest = j
		first = arr[i]
		second = arr[smallest]
		arr[i] = second
		arr[smallest] = first
		i += 1
	return arr


def book_selection_sort(arr):
	length = len(arr)
	for i in range(length - 1):
		smallest = i
		for j in range(i + 1, length):
			if arr[j] < arr[smallest]:
				smallest = j
		first = arr[i]
		second = arr[smallest]
		arr[i] = second
		arr[smallest] = first
	return arr


def selection_sort_with_prints(arr):
	# Iterate over n - 1 elements of the array.

	# In first iteration find smallest element of the array.
	# Exchange it with element in first position of the array.

	# In second iteration find smallest element of the array[1:].
	# Exchange it with the element in second position of the array.

	# Continue until reaching WHAT? n - 1
	length = len(arr)
	length_minus_one = length - 1
	i = 0
	while i < length_minus_one:
		first = arr[i]
		smallest = first
		print("first", first)
		for j in range(i + 1, length):
			print("arr[j]", arr[j])
			if arr[j] < smallest:
				print("new smallest", arr[j])
				smallest = arr[j]
		print("before", arr)
		idx = arr.index(smallest)
		arr[i] = smallest
		arr[idx] = first
		print("after", arr)
		i += 1
	return arr
