import math
import pdb
import sys
sys.path.append("C:\\repos\programming")

from operator import gt, lt

from data_structures.infinity.structure import NegativeInfinity


def safe_list_item_getter(func):
	def wrap(*args):
		try:
			return func(*args)
		except IndexError:
			return None
	return wrap


class Node(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
		self.heap = None
		self.idx = None

	def __str__(self):
		return "<Node (%s)>" % self.value

	def __repr__(self):
		return "<Node (%s) %s>" % (self.value, id(self))

	def get_left_index(self):
		return 2 * self.idx + 1

	def get_right_index(self):
		return 2 * self.idx + 2

	@property
	@safe_list_item_getter
	def parent(self):
		if self.idx == 0:
			return None
		return self.heap.nodes[self.parent_idx]

	@property
	def parent_idx(self):
		return (self.idx - 1) // 2

	def is_left(self, node):
		if not node:
			raise ValueError("Must be %s type." % type(self))
		return node is self.left

	def is_right(self, node):
		if not node:
			raise ValueError("Must be %s type." % type(self))
		return node is self.right

	def set_child(self, node):
		if self.left and self.right:
			raise ValueError("Children set already.")
		if self.left:
			self.right = node
		else:
			self.left = node


class Heap(object):
	def __init__(self, nodes=None):
		if nodes:
			self.create_tree(nodes)
		else:
			self.nodes = []
		self.size = len(self.nodes)

	@property
	def height(self):
		return math.floor(math.log(self.size, 2))

	def create_tree(self, nodes):
		value = 1
		for idx, node in enumerate(nodes):
			left_idx, right_idx = self._calculate_children_indexes(idx, value)
			left_node = self.get_node_by_idx(left_idx, nodes)
			self._set_node_data(left_node, left_idx)
			right_node = self.get_node_by_idx(right_idx, nodes)
			self._set_node_data(right_node, right_idx)
			node.left = left_node
			node.right = right_node
			self._set_node_data(node, idx)
			# If there are no more nodes to set
			if not all([left_node, right_node]):
				break
			value += 1
		self.nodes = nodes

	def _calculate_children_indexes(self, idx, value):
		left_idx = idx + value
		right_idx = left_idx + 1
		return left_idx, right_idx

	def _set_node_data(self, node, idx):
		if node:
			node.idx = idx
			node.heap = self

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
		root_node = self.get_node_by_idx(i)
		l_idx = root_node.get_left_index()
		r_idx = root_node.get_right_index()
		left_node = self.get_node_by_idx(l_idx)
		right_node = self.get_node_by_idx(r_idx)
		if l_idx <= self.size and left_node and root_node and condition_operator(left_node.value, root_node.value):
			smallest_or_largest = l_idx
		else:
			smallest_or_largest = i
		smallest_or_largest_node = self.get_node_by_idx(smallest_or_largest)
		if r_idx <= self.size and right_node and smallest_or_largest_node and condition_operator(right_node.value, smallest_or_largest_node.value):
			smallest_or_largest = r_idx

		if smallest_or_largest != i:
			self.exchange(smallest_or_largest, i)
			self._heapify(smallest_or_largest, condition_operator)

	def exchange(self, i, j):
		ith_node = self.get_node_by_idx(i)
		jth_node = self.get_node_by_idx(j)
		parent, child = self.define_parent_and_child(ith_node, jth_node)
		if parent and child:
			self.exchange_parent_child(parent, child)
		else:
			self.exchange_distant_nodes(ith_node, jth_node)

	def exchange_parent_child(self, parent, child):
		is_left = parent.is_left(child)
		p_parent = parent.parent
		p_left = parent.left
		p_right = parent.right

		c_left = child.left
		c_right = child.right
		if p_parent:
			self.set_parent_new_child(p_parent, parent, child)

		parent.left = c_left
		parent.right = c_right

		if is_left:
			child.left = parent
			child.right = p_right
		else:
			child.left = p_left
			child.right = parent

		i = parent.idx
		j = child.idx
		self.nodes[i] = child
		child.idx = i
		self.nodes[j] = parent
		parent.idx = j

	def define_parent_and_child(self, first, second):
		if first is second.parent:
			return first, second
		elif second is first.parent:
			return second, first
		else:
			return None, None

	def exchange_distant_nodes(self, ith_node, jth_node):
		i_parent = ith_node.parent
		i_left = ith_node.left
		i_right = ith_node.right

		j_parent = jth_node.parent
		j_left = jth_node.left
		j_right = jth_node.right

		# Set ith_node's new values
		ith_node.left = j_left
		ith_node.right = j_right
		if i_parent:
			self.set_parent_new_child(i_parent, ith_node, jth_node)

		# Set jth_node's new values
		jth_node.left = i_left
		jth_node.right = i_right
		if j_parent:
			self.set_parent_new_child(j_parent, jth_node, ith_node)

		# Update heap
		i = ith_node.idx
		j = jth_node.idx
		self.nodes[i] = jth_node
		jth_node.idx = i
		self.nodes[j] = ith_node
		ith_node.idx = j

	def set_parent_new_child(self, parent, node, new_node):
		if parent.is_left(node):
			parent.left = new_node
		else:
			parent.right = new_node

	def build_max_heap(self):
		self._build_heap(self.max_heapify)

	def build_min_heap(self):
		self._build_heap(self.min_heapify)

	def _build_heap(self, handler):
		half = self.size // 2
		for i in range(half, -1, -1):
			handler(i)

	def increase_key(self, i, value):
		node = self.get_node_by_idx(i)
		if node.value > value:
			raise ValueError("New value is smaller than current value.")
		node.value = value
		parent = node.parent
		if not parent:
			return
		while i > 0 and parent and parent.value < node.value:
			parent_idx = node.parent_idx
			self.exchange(i, parent_idx)
			parent = self.get_node_by_idx(node.parent_idx)
			i = parent_idx

	def max_heap_insert(self, value):
		node = Node(NegativeInfinity())
		node.heap = self
		self.nodes.append(node)
		node.idx = self.size
		parent = node.parent
		parent.set_child(node)
		self.size += 1
		self.increase_key(self.size - 1, value)


class MaxPriorityQueue(Heap):
	@safe_list_item_getter
	def maximum(self):
		return self.nodes[0]

	@safe_list_item_getter
	def extract_max(self):
		if self.size < 1:
			raise ValueError("Queue is empty.")
		self.exchange(0, -1)

		maximum = self.nodes.pop(-1)
		self.size -= 1
		self.max_heapify(0)
		maximum.left = None
		maximum.right = None
		return maximum
