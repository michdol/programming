class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def safe_list_item_getter(func):
	def wrap(*args):
		try:
			return func(*args)
		except IndexError:
			return None
	return wrap


class Heap(object):
	def __init__(self):
		self.nodes = []

	@staticmethod
	def get_left_index(i):
		return 2 * i + 1

	@staticmethod
	def get_right_index(i):
		return 2 * i + 2

	@safe_list_item_getter
	def left(self, i):
		return self.nodes[self.get_left_index(i)]

	@safe_list_item_getter
	def right(self, i):
		return self.nodes[self.get_right_index(i)]

	@safe_list_item_getter
	def parent(self, i):
		return self.nodes[(i - 1) // 2]

	@safe_list_item_getter
	def get_node_by_idx(self, i):
		return self.nodes[i]

	def exchange(self, i, j):
		ith_node = self.get_node_by_idx(i)
		jth_node = self.get_node_by_idx(j)
		i_left = ith_node.left
		i_right = ith_node.right
		j_left = jth_node.left
		j_right = jth_node.right
		ith_node.left = j_left
		ith_node.right = j_right
		jth_node.left = i_left
		jth_node.right = i_right
		self.nodes[i] = jth_node
		self.nodes[j] = ith_node

	def max_heapify(self, i):
		l = self.get_left_index(i)
		r = self.get_right_index(i)
		heap_size = len(self.nodes)
		root_node = self.get_node_by_idx(i)
		left_node = self.get_node_by_idx(l)
		right_node = self.get_node_by_idx(r)
		if l <= heap_size and left_node and root_node and left_node.value > root_node.value:
			largest = l
		else:
			largest = i
		if r <= heap_size and right_node and root_node and right_node.value > root_node.value:
			largest = r
		if largest != i:
			self.exchange(largest, i)
			self.max_heapify(largest)
