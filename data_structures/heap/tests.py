from unittest import TestCase, main

from structure import Node, Heap


class HeapTest(TestCase):

	def setUp(self):
		"""
				5
			  /   \
			 4     3
		   /  \
		  2    1
		"""
		self.root = Node(5)
		self.root.left = Node(4)
		self.root.right = Node(3)
		self.root.left.left = Node(2)
		self.root.left.right = Node(1)

		self.heap = Heap()
		self.heap.nodes = [
			self.root,
			self.root.left,
			self.root.right,
			self.root.left.left,
			self.root.left.right
		]

	def test_parent(self):
		parent = self.heap.parent(1)
		self.assertIs(parent, self.root)
		parent = self.heap.parent(2)
		self.assertIs(parent, self.root)
		parent = self.heap.parent(3)
		self.assertIs(parent, self.root.left)
		parent = self.heap.parent(4)
		self.assertIs(parent, self.root.left)

	def test_left(self):
		left = self.heap.left(0)
		self.assertIs(left, self.root.left)
		left = self.heap.left(1)
		self.assertIs(left, self.root.left.left)
		left = self.heap.left(2)
		self.assertIsNone(left)

	def test_right(self):
		right = self.heap.right(0)
		self.assertIs(right, self.root.right)
		right = self.heap.right(1)
		self.assertIs(right, self.root.left.right)
		right = self.heap.right(2)
		self.assertIsNone(right)

	def test_max_heapify(self):
		"""
					4
				  /   \
				 5     3
		"""
		self.root = Node(4)
		self.root.left = Node(5)
		self.root.right = Node(3)

		self.heap = Heap()
		self.heap.nodes = [self.root, self.root.left, self.root.right]

		self.heap.max_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 5)
		self.assertEqual(self.heap.nodes[1].value, 4)
		self.assertEqual(self.heap.nodes[2].value, 3)
		self.assertIs(self.heap.parent(1).value, 5)


if __name__ == "__main__":
	main()
