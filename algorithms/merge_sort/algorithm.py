import pdb
sentinel = 99999999999


def merge(arr, p, q, r):
	z = q - p + 1
	print(p, q, r, z)
	left = arr[p:z]
	right = arr[z:]
	left.append(sentinel)
	right.append(sentinel)
	i = 0
	j = 0
	for k in range(p, r + 1):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1


def merge_sort(arr, p, r):
	if p < r:
		q = int((p + (r - 1)) / 2)
		merge_sort(arr, p, q)
		merge_sort(arr, q + 1, r)
		merge(arr, p, q, r)
