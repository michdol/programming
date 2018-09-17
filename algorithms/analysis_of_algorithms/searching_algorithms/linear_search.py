
def linear_search(array, target):
	# idx is number of operations performed.
	for idx, item in enumerate(array, start=1):
		if item == target:
			return idx, item
	return idx, -1


number = 30
best_case = [30, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
avg_case = [1, 1, 1, 1, 1, 1, 30, 1, 1, 1, 1, 1, 1]
worst_case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30]

best_case_result = linear_search(best_case, number)
avg_case_result = linear_search(avg_case, number)
worst_case_result = linear_search(worst_case, number)

# print("Length of all arrays: ", len(best_case))
# print(best_case_result, " O(1)")
# print(avg_case_result, " O(?)")
# print(worst_case_result, " O(n)")
#
