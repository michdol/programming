class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return "Node <%d>" % self.data


class UnoptimizedLinkedList(object):
	current = None

	def __init__(self, iterable=None):
		self.head = None
		if iterable is not None:
			if not self.is_iterable(iterable):
				raise TypeError("{} not iterable".format(iterable))
			self.convert_from_iterable(iterable)

	def __str__(self):
		tmp = self.head
		data = []
		while tmp and len(data) < 4:
			data.append(tmp.data.__str__())
			tmp = tmp.next
		return "Linked list <{}, ...>".format(', '.join(data))

	def __iter__(self):
		return self

	def __next__(self):
		if self.head is None:
			raise StopIteration()
		if self.current is None:
			self.current = self.head
			return self.current
		else:
			self.current = self.current.next
		if self.current is None:
			raise StopIteration()
		return self.current

	def __len__(self):
		count = 0
		tmp = self.head
		while tmp:
			count += 1
			tmp = tmp.next
		return count

	def is_iterable(self, iterable):
		try:
			iter(iterable)
		except TypeError:
			return False
		return True

	def convert_from_iterable(self, iterable):
		if len(iterable) < 1:
			return
		self.head = Node(iterable[0])
		prev_node = self.head
		for data in iterable[1:]:
			new_node = Node(data)
			prev_node.next = new_node
			prev_node = new_node

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
			raise ValueError("Previous node must be Node")
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
			raise ValueError("node argument must be Node")
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

	def get(self, data, default=None):
		tmp = self.head
		while tmp:
			if tmp.data == data:
				return tmp
			tmp = tmp.next
		return default

	def swap_nodes(self, x, y):
		x_node = self.get(x)
		y_node = self.get(y)
		x_is_head = x_node is self.head
		y_is_head = y_node is self.head
		adjacent_nodes = x_node.next is y_node or y_node.next is x_node
		if adjacent_nodes:
			if x_node.next is y_node:
				left = x_node
				right = y_node
			else:
				left = y_node
				right = x_node

			left_previous_node = self.get_prev_node(left)
			right_next_node = right.next
			if isinstance(left_previous_node, Node):
				left_previous_node.next = right
			right.next = left
			left.next = right_next_node
		else:
			x_prev_node = self.get_prev_node(x_node)
			x_next_node = x_node.next

			y_prev_node = self.get_prev_node(y_node)
			y_next_node = y_node.next

			if isinstance(x_prev_node, Node):
				x_prev_node.next = y_node
			if isinstance(x_next_node, Node):
				y_node.next = x_next_node
			if isinstance(y_prev_node, Node):
				y_prev_node.next = x_node
			if isinstance(y_next_node, Node):
				x_node.next = y_next_node

		if x_is_head:
			self.head = y_node
		elif y_is_head:
			self.head = x_node

	def reverse(self):
		if self.head is None:
			return
		previous = self.head
		current = previous.next
		while True:
			next_ = current.next
			current.next = previous
			previous.next = None
			previous = current
			current = next_
			if next_ is None:
				break
