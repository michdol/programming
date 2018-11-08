matrix_a = [
	[1, 2],
	[3, 4]
]

matrix_b = [
	[5, 6],
	[7, 8]
]


def square_matrix_multiply_recursive(a, b):
	n = len(a)
	c = [[0, 0], [0, 0]]
	if n == 1:
		return a[0][0] * b[0][0]
	else:
		c[0][0] = square_matrix_multiply_recursive([[a[0][0]]], [[b[0][0]]]) + square_matrix_multiply_recursive([[a[0][1]]], [[b[1][0]]])
		c[0][1] = square_matrix_multiply_recursive([[a[0][0]]], [[b[0][1]]]) + square_matrix_multiply_recursive([[a[0][1]]], [[b[1][1]]])
		c[1][0] = square_matrix_multiply_recursive([[a[1][0]]], [[b[0][0]]]) + square_matrix_multiply_recursive([[a[1][1]]], [[b[1][0]]])
		c[1][1] = square_matrix_multiply_recursive([[a[1][0]]], [[b[0][1]]]) + square_matrix_multiply_recursive([[a[1][1]]], [[b[1][1]]])
	return c


print(square_matrix_multiply_recursive(matrix_a, matrix_b))
