

def insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		# Insert array[i] into the sorted sequence array[0:i - 1]
		j = i - 1
		while j >= 0 and array[j] > key:
			array[j + 1] = array[j]
			j = j - 1
		array[j + 1] = key
	return array


arr = [4, 2, 5, 7, 1, 6, 3]
# Start for loop at second index of input array (i = 1).
# At index 1 is the element to be moved first (arr[i] = 2).
# Get first item "to the left" from the key with index j = i - 1 (arr[j] = 4).
# Condition of while loop is True.
# Move arr[j] to the right (In this case it is where the key is).
# Decrease j by one (while loop's condition is no longer True since j < 0).
# Insert the key on last j + 1.
# First iteration of for loop finished.


def descending_insertion_sort(array):
	for i in range(1, len(array)):
		key = array[i]
		# Insert array[i] into the sorted sequence array[0:i - 1]
		j = i - 1
		while j >= 0 and array[j] < key:
			array[j + 1] = array[j]
			j = j - 1
		array[j + 1] = key
	return array


def linear_search(array, num):
	index = None
	i = 0
	length = len(array)
	while i < length and index is None:
		if array[i] == num:
			index = i
		i = i + 1

	return index


def solution_linear_search(array, num):
	for i in range(len(array)):
		if array[i] == num:
			return i
	return None
