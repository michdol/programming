class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList(object):
	def __init__(self):
		self.head = None

	def __str__(self):
		tmp = self.head
		data = []
		while tmp and len(data) < 4:
			data.append(tmp.data.__str__())
			tmp = tmp.next
		return "Linked list <{}, ...>".format(', '.join(data))

	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def append(self, data):
		"""
		Unoptimized method appending new node to the end of the list.
		If it's not empty its complexity is O(n) since it traverses through whole list to the last node.
		"""
		new_node = Node(data)
		# If list is empty, set new_node as head of the list.
		if self.head is None:
			self.head = new_node
			return

		last_node = self.get_last_node()
		last_node.next = new_node

	def insert(self, prev_node, data):
		if self.head is None:
			raise ValueError("Cannot insert while the list is empty")
		if not isinstance(prev_node, Node):
			raise ValueError("Previous node must be {}".format(Node))
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete(self, data):
		tmp = self.head
		while tmp is not None:
			if tmp.data == data:
				prev_node = self.get_prev_node(tmp)
				if prev_node is None:
					self.head = tmp.next
				else:
					prev_node.next = tmp.next
				del tmp
				return
			tmp = tmp.next
		raise ValueError("{} not present in the list".format(data))

	def delete_at_index(self, index):
		if self.head is None:
			raise IndexError("\delete from empty list")
		if index == 0:
			return self.delete_head()

		prev_node = self.head
		tmp = self.head.next
		for i in range(index - 1):
			prev_node = tmp
			tmp = self.get_next_node_or_index_error(tmp)
		# At this point tmp is element at given index.
		if tmp is None:
			raise IndexError("list index out of range")
		prev_node.next = tmp.next
		del tmp

	def delete_head(self):
		tmp = self.head
		self.head = tmp.next
		del tmp

	def get_next_node_or_index_error(self, node):
		try:
			return node.next
		except AttributeError:
			raise IndexError("list index out of range")

	def get_prev_node(self, node):
		if self.head is None:
			raise ValueError("the list is empty")
		if not isinstance(node, Node):
			raise ValueError("Node argument must be {}".format(Node))
		prev_node = self.head
		while prev_node.next is not None:
			if prev_node.next is node:
				return prev_node
			prev_node = prev_node.next

	def get_last_node(self):
		tmp = self.head
		if tmp is None:
			return
		while tmp.next is not None:
			tmp = tmp.next
		return tmp
