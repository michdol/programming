from linear_search import linear_search

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

number = 30
ranges = [10, 100, 200, 500, 1000]
cases = [
	[1 for _ in range(i)] + [30]
	for i in ranges
]

# cases = [
# 	[1 for _ in range(15)] + [30],
# 	[1 for _ in range(100)] + [30],
# 	[1 for _ in range(1000)] + [30],
# ]

results = []
lens = []
for case in cases:
	lens.append(len(case))
	res = linear_search(case, number)
	results.append(res[0])

data = {
	'n': lens,
	'worst case': results
}
df = pd.DataFrame(data)
df.plot(x='n', y='worst case', style='k--')
plt.show()

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
