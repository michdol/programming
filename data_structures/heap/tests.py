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
					  16
				   /     \
				 4        10
				/ \      /  \
			  14  7     9   3
			  /\  /
		     2 8 1

					  16
				   /     \
				 14       10
				/ \      /  \
			   8  7     9   3
			  /\  /
		     2 4 1
		"""
		nodes = [Node(i) for i in [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]]
		self.heap = Heap(nodes)
		self.heap.max_heapify(1)
		self.assertEqual(self.heap.nodes[0].value, 16)
		self.assertEqual(self.heap.nodes[1].value, 14)
		self.assertEqual(self.heap.nodes[2].value, 10)
		self.assertEqual(self.heap.nodes[3].value, 8)
		self.assertEqual(self.heap.nodes[4].value, 7)
		self.assertEqual(self.heap.nodes[5].value, 9)
		self.assertEqual(self.heap.nodes[6].value, 3)
		self.assertEqual(self.heap.nodes[7].value, 2)
		self.assertEqual(self.heap.nodes[8].value, 4)
		self.assertEqual(self.heap.nodes[9].value, 1)

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
					  16
				   /     \
				 4        10
				/  \     /  \
			  14   7    9   3
		     / \  /
		    2  8 1

					  4
				   /     \
				 7       10
				/ \     /  \
			   14  1   9   3
			  /\  /
		     2 8 16
		"""
		nodes = [Node(i) for i in [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]]
		self.heap = Heap(nodes)
		self.heap.min_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 4)
		self.assertEqual(self.heap.nodes[1].value, 7)
		self.assertEqual(self.heap.nodes[2].value, 10)
		self.assertEqual(self.heap.nodes[3].value, 14)
		self.assertEqual(self.heap.nodes[4].value, 1)
		self.assertEqual(self.heap.nodes[5].value, 9)
		self.assertEqual(self.heap.nodes[6].value, 3)
		self.assertEqual(self.heap.nodes[7].value, 2)
		self.assertEqual(self.heap.nodes[8].value, 8)
		self.assertEqual(self.heap.nodes[9].value, 16)

	def test_build_max_heap(self):
		"""
					  4
				   /     \
				 1        3
				/ \      /  \
			   2  16    9   10
			  /\  /
		    14 8 7

					  16
				   /     \
				 14        10
				/ \      /  \
			   8  7    9    3
			  /\  /
		     2 4 1
		"""
		self.heap = Heap([Node(i) for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]])
		self.heap.build_max_heap()
		self.assertEqual(self.heap.nodes[0].value, 16)
		self.assertEqual(self.heap.nodes[1].value, 14)
		self.assertEqual(self.heap.nodes[2].value, 10)
		self.assertEqual(self.heap.nodes[3].value, 8)
		self.assertEqual(self.heap.nodes[4].value, 7)
		self.assertEqual(self.heap.nodes[5].value, 9)
		self.assertEqual(self.heap.nodes[6].value, 3)
		self.assertEqual(self.heap.nodes[7].value, 2)
		self.assertEqual(self.heap.nodes[8].value, 4)
		self.assertEqual(self.heap.nodes[9].value, 1)

	def test_build_min_heap(self):
		"""
					  4
				   /     \
				 1        3
				/ \      /  \
			   2  16    9   10
			  /\  /
		    14 8 7

					  1
				   /     \
				 2        3
				/ \      / \
			   4   7    9  10
			  /\  /
		    14 8 16
		"""
		self.heap = Heap([Node(i) for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]])
		self.heap.build_min_heap()
		self.assertEqual(self.heap.nodes[0].value, 1)
		self.assertEqual(self.heap.nodes[1].value, 2)
		self.assertEqual(self.heap.nodes[2].value, 3)
		self.assertEqual(self.heap.nodes[3].value, 4)
		self.assertEqual(self.heap.nodes[4].value, 7)
		self.assertEqual(self.heap.nodes[5].value, 9)
		self.assertEqual(self.heap.nodes[6].value, 10)
		self.assertEqual(self.heap.nodes[7].value, 14)
		self.assertEqual(self.heap.nodes[8].value, 8)
		self.assertEqual(self.heap.nodes[9].value, 16)


if __name__ == "__main__":
	main()
