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
					2
				  /   \
				 3     4
				/ \
			   5   1

					5
				  /   \
				 4     2
				/ \
			   3   1
		"""
		self.root = Node(2)
		self.root.left = Node(3)
		self.root.right = Node(4)
		self.root.left.left = Node(5)
		self.root.left.right = Node(1)

		self.heap = Heap()
		self.heap.nodes = [self.root, self.root.left, self.root.right, self.root.left.left, self.root.left.right]

		self.heap.max_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 4)
		self.assertEqual(self.heap.nodes[1].value, 3)
		self.assertEqual(self.heap.nodes[2].value, 2)
		self.assertEqual(self.heap.nodes[3].value, 5)
		self.assertEqual(self.heap.nodes[4].value, 1)
		self.heap.max_heapify(1)
		self.assertEqual(self.heap.nodes[0].value, 4)
		self.assertEqual(self.heap.nodes[1].value, 5)
		self.assertEqual(self.heap.nodes[2].value, 2)
		self.assertEqual(self.heap.nodes[3].value, 3)
		self.assertEqual(self.heap.nodes[4].value, 1)
		self.heap.max_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 5)
		self.assertEqual(self.heap.nodes[1].value, 4)
		self.assertEqual(self.heap.nodes[2].value, 2)
		self.assertEqual(self.heap.nodes[3].value, 3)
		self.assertEqual(self.heap.nodes[4].value, 1)

	def test_create_tree(self):
		"""
						0
					/      \
				  1          2
				/  \      /    \
			   3    4    5      6
			  /\   /\   / \    /\
			 7 8  9 10 11 12 13 14

		0 - 1, 2	(+1)
		1 - 3, 4	(+2)
		2 - 5, 6	(+3)
		3 - 7, 8	(+4)
		4 - 9, 10	(+5)
		5 - 11, 12	(+6)
		6 - 13, 14	(+7)
		"""
		nodes = [Node(i) for i in range(14)]
		heap = Heap(nodes)
		self.assertEqual(heap.nodes, nodes)
		root = heap.nodes[0]
		self.assertEqual(root.left, heap.nodes[1])
		self.assertEqual(root.right, heap.nodes[2])
		self.assertEqual(root.left.left, heap.nodes[3])
		self.assertEqual(root.left.right, heap.nodes[4])
		self.assertEqual(root.right.left, heap.nodes[5])
		self.assertEqual(root.right.right, heap.nodes[6])
		self.assertEqual(root.left.left.left, heap.nodes[7])
		self.assertEqual(root.left.left.right, heap.nodes[8])
		self.assertEqual(root.left.right.left, heap.nodes[9])
		self.assertEqual(root.left.right.right, heap.nodes[10])
		self.assertEqual(root.right.left.left, heap.nodes[11])
		self.assertEqual(root.right.left.right, heap.nodes[12])
		self.assertEqual(root.right.right.left, heap.nodes[13])
		self.assertIsNone(root.right.right.right)

	def test_min_heapify(self):
		"""
					5
				  /   \
				 3     4
				/ \
			   2   1

					1
				  /   \
				 2     5
				/ \
			   3   4
		"""
		self.heap = Heap([Node(i) for i in [5, 3, 4, 2, 1]])

		self.heap.min_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 4)
		self.assertEqual(self.heap.nodes[1].value, 3)
		self.assertEqual(self.heap.nodes[2].value, 5)
		self.assertEqual(self.heap.nodes[3].value, 2)
		self.assertEqual(self.heap.nodes[4].value, 1)
		self.heap.min_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 3)
		self.assertEqual(self.heap.nodes[1].value, 1)
		self.assertEqual(self.heap.nodes[2].value, 5)
		self.assertEqual(self.heap.nodes[3].value, 2)
		self.assertEqual(self.heap.nodes[4].value, 4)
		self.heap.min_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 1)
		self.assertEqual(self.heap.nodes[1].value, 2)
		self.assertEqual(self.heap.nodes[2].value, 5)
		self.assertEqual(self.heap.nodes[3].value, 3)
		self.assertEqual(self.heap.nodes[4].value, 4)


if __name__ == "__main__":
	main()
