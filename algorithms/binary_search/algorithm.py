

def binary_search(arr, l, r, num):
	if r >= l:
		mid = (l + (r + 1)) // 2
		if arr[mid] == num:
			return mid
		elif arr[mid] < num:
			return binary_search(arr, mid + 1, r, num)
		elif arr[mid] > num:
			return binary_search(arr, l, mid - 1, num)
	else:
		return -1


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search_with_merge_sort():
	raise NotImplementedError("do me")


binary_search_with_merge_sort()g