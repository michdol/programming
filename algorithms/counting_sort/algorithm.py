
a = [2, 1, 3]


def counting_sort(A, B, k):
	C = [0 for _ in range(k+1)]
	for j in range(0, len(A)):
		C[A[j]] += 1
	print(C)
	for i in range(0, len(C)):
		C[i] = C[i] + C[i - 1]	# C[i - 1] in python might not work as expected
	print(C)


b = []

counting_sort(a, b, 3)

#    0  1  2  3
C = [0, 0, 0, 0]
C = [0, 1, 1, 1]
C = [1, 2, 3, 4]
