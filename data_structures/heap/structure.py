import pdb

from operator import gt, lt


class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def __str__(self):
		return "<Node (%d)>" % self.value


def safe_list_item_getter(func):
	def wrap(*args):
		try:
			return func(*args)
		except IndexError:
			return None
	return wrap


class Heap(object):
	def __init__(self, nodes=None):
		if nodes:
			self.create_tree(nodes)
		else:
			self.nodes = []
		self.size = len(self.nodes)

	def create_tree(self, nodes):
		value = 1
		for idx, node in enumerate(nodes):
			left_idx, right_idx = self._calculate_children_indexes(idx, value)
			left_node = self.get_node_by_idx(left_idx, nodes)
			right_node = self.get_node_by_idx(right_idx, nodes)
			node.left = left_node
			node.right = right_node
			# If there are no more nodes to set
			if not all([left_node, right_node]):
				break
			value += 1
		self.nodes = nodes

	def _calculate_children_indexes(self, idx, value):
		left_idx = idx + value
		right_idx = left_idx + 1
		return left_idx, right_idx

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
	def get_node_by_idx(self, i, nodes=None):
		if not nodes:
			nodes = self.nodes
		return nodes[i]

	def max_heapify(self, i):
		self._heapify(i, gt)

	def min_heapify(self, i):
		self._heapify(i, lt)

	def _heapify(self, i, condition_operator):
		if not self.size:
			self.size = len(self.nodes)
		root_node = self.get_node_by_idx(i)
		l_idx = self.get_left_index(i)
		r_idx = self.get_right_index(i)
		left_node = self.get_node_by_idx(l_idx)
		right_node = self.get_node_by_idx(r_idx)
		if l_idx <= self.size and left_node and root_node and condition_operator(left_node.value, root_node.value):
			smallest_or_largest = l_idx
		else:
			smallest_or_largest = i
		if r_idx <= self.size and right_node and root_node and condition_operator(right_node.value, root_node.value):
			smallest_or_largest = r_idx

		if smallest_or_largest != i:
			self.exchange(smallest_or_largest, i)
			self._heapify(smallest_or_largest, condition_operator)

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
