import pdb
from unittest import TestCase, main

from structure import Node, Heap, MaxPriorityQueue


class NodeTest(TestCase):
	def test_parent(self):
		first, second, third, fourth = Node(1), Node(2), Node(3), Node(4)
		heap = Heap([first, second, third, fourth])

		parent = first.parent
		self.assertIsNone(parent)

		parent = second.parent
		self.assertIs(parent, first)
		self.assertIs(parent, heap.nodes[0])

		parent = third.parent
		self.assertIs(parent, first)
		self.assertIs(parent, heap.nodes[0])

		parent = fourth.parent
		self.assertIs(parent, second)
		self.assertIs(parent, heap.nodes[1])

	def test_get_left_idx__get_right_idx(self):
		first, second, third, fourth = Node(1), Node(2), Node(3), Node(4)
		Heap([first, second, third, fourth])

		idx = first.get_left_index()
		self.assertEqual(idx, 1)
		idx = first.get_right_index()
		self.assertEqual(idx, 2)

		idx = second.get_left_index()
		self.assertEqual(idx, 3)
		idx = second.get_right_index()
		self.assertEqual(idx, 4)

		idx = third.get_left_index()
		self.assertEqual(idx, 5)
		idx = third.get_right_index()
		self.assertEqual(idx, 6)

		idx = fourth.get_left_index()
		self.assertEqual(idx, 7)
		idx = fourth.get_right_index()
		self.assertEqual(idx, 8)

	def test_is_left__is_right(self):
		first, second, third, fourth = Node(1), Node(2), Node(3), Node(4)
		Heap([first, second, third, fourth])

		self.assertTrue(first.is_left(second))
		self.assertFalse(first.is_right(second))

		self.assertTrue(second.is_left(fourth))
		self.assertFalse(second.is_right(third))

		with self.assertRaises(ValueError):
			second.is_left(None)

		with self.assertRaises(ValueError):
			second.is_right(None)


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

	def test_max_heapify_three(self):
		nodes = [Node(i) for i in [1, 3, 2]]
		self.heap = Heap(nodes)
		self.heap.max_heapify(0)
		self.assertEqual(self.heap.nodes[0].value, 3)
		self.assertEqual(self.heap.nodes[0].left.value, 1)
		self.assertEqual(self.heap.nodes[0].right.value, 2)

	def test_exchange_parent_child(self):
		"""
					  1
				   /    \
				 2       3
				/ \     / \
			  4    5   6   7
			 /\   /\   /\  /\
		    8  9

					  1
				   /    \
				 4       3
				/ \     / \
			  2    5   6   7
			 /\   /\   /\  /\
		    8  9
		"""
		nodes = [Node(i) for i in range(1, 18)]
		self.heap = Heap(nodes)
		self.heap.exchange(1, 3)

		self.assertEqual(self.heap.nodes[0].value, 1)
		self.assertEqual(self.heap.nodes[0].left.value, 4)
		self.assertEqual(self.heap.nodes[0].right.value, 3)
		self.assertEqual(self.heap.nodes[1].value, 4)
		# import pdb
		# pdb.set_trace()
		self.assertEqual(self.heap.nodes[1].left.value, 2)
		self.assertEqual(self.heap.nodes[1].right.value, 5)
		self.assertEqual(self.heap.nodes[3].value, 2)
		self.assertEqual(self.heap.nodes[3].left.value, 8)
		self.assertEqual(self.heap.nodes[3].right.value, 9)

		self.assertEqual(self.heap.nodes[1].parent.value, 1)
		self.assertEqual(self.heap.nodes[3].parent.value, 4)
		self.assertEqual(self.heap.nodes[4].parent.value, 4)
		self.assertEqual(self.heap.nodes[7].parent.value, 2)
		self.assertEqual(self.heap.nodes[8].parent.value, 2)

	def test_exchange_distant_nodes(self):
		"""
					  1
				   /    \
				 2       3
				/ \     / \
			  4    5   6   7
			 /\   /\   /\  /\
		    8  9
		   /\
		  16 17

					  1
				   /    \
				 8       3
				/ \     / \
			  4    5   6   7
			 /\   /\   /\  /\
		    2  9
		   /\
		  16 17
		"""
		nodes = [Node(i) for i in range(1, 18)]
		self.heap = Heap(nodes)
		self.heap.exchange_distant_nodes(self.heap.nodes[1], self.heap.nodes[7])
		self.assertEqual(self.heap.nodes[1].value, 8)
		self.assertEqual(self.heap.nodes[1].left.value, 4)
		self.assertEqual(self.heap.nodes[1].right.value, 5)
		self.assertEqual(self.heap.nodes[3].value, 4)
		self.assertEqual(self.heap.nodes[3].left.value, 2)
		self.assertEqual(self.heap.nodes[3].right.value, 9)
		self.assertEqual(self.heap.nodes[7].value, 2)
		self.assertEqual(self.heap.nodes[7].left.value, 16)
		self.assertEqual(self.heap.nodes[7].right.value, 17)

		self.assertEqual(self.heap.nodes[1].parent.value, 1)
		self.assertEqual(self.heap.nodes[3].parent.value, 8)
		self.assertEqual(self.heap.nodes[4].parent.value, 8)
		self.assertEqual(self.heap.nodes[7].parent.value, 4)
		self.assertEqual(self.heap.nodes[15].parent.value, 2)
		self.assertEqual(self.heap.nodes[16].parent.value, 2)

	def test_define_parent_and_child(self):
		first = Node(1)
		second = Node(2)
		heap = Heap([first, second, Node(3), Node(4)])
		parent, child = heap.define_parent_and_child(heap.nodes[0], heap.nodes[1])
		self.assertIs(parent, first)
		self.assertIs(child, second)
		parent, child = heap.define_parent_and_child(heap.nodes[1], heap.nodes[0])
		self.assertIs(parent, first)
		self.assertIs(child, second)
		parent, child = heap.define_parent_and_child(heap.nodes[0], heap.nodes[3])
		self.assertIsNone(parent)
		self.assertIsNone(child)

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
		self.assertEqual(root.idx, 0)
		self.assertEqual(root.left.left, heap.nodes[3])
		self.assertEqual(root.left.right, heap.nodes[4])
		self.assertEqual(root.left.idx, 1)
		self.assertEqual(root.right.left, heap.nodes[5])
		self.assertEqual(root.right.right, heap.nodes[6])
		self.assertEqual(root.right.idx, 2)
		self.assertEqual(root.left.left.left, heap.nodes[7])
		self.assertEqual(root.left.left.right, heap.nodes[8])
		self.assertEqual(root.left.left.idx, 3)
		self.assertEqual(root.left.right.left, heap.nodes[9])
		self.assertEqual(root.left.right.right, heap.nodes[10])
		self.assertEqual(root.left.right.idx, 4)
		self.assertEqual(root.right.left.left, heap.nodes[11])
		self.assertEqual(root.right.left.right, heap.nodes[12])
		self.assertEqual(root.right.left.idx, 5)
		self.assertEqual(root.right.right.left, heap.nodes[13])
		self.assertEqual(root.right.right.idx, 6)
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

	def test_height_of_heap(self):
		self.heap = Heap([Node(i) for i in [4]])
		self.assertEqual(self.heap.height, 0)

		self.heap = Heap([Node(i) for i in [4, 1]])
		self.assertEqual(self.heap.height, 1)

		self.heap = Heap([Node(i) for i in [4, 1, 3]])
		self.assertEqual(self.heap.height, 1)

		self.heap = Heap([Node(i) for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]])
		self.assertEqual(self.heap.height, 3)

		self.heap = Heap([Node(i) for i in [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 15, 17, 18, 19, 20, 21]])
		self.assertEqual(self.heap.height, 4)


class MaxPriorityQueueTest(TestCase):
	def test_maximum(self):
		queue = MaxPriorityQueue([Node(i) for i in [4, 3, 2, 1]])
		maximum = queue.maximum()
		self.assertEqual(maximum.value, 4)
		self.assertEqual(maximum.left.value, 3)
		self.assertEqual(maximum.right.value, 2)

		empty_queue = MaxPriorityQueue()
		self.assertIsNone(empty_queue.maximum())

	def test_extract_max(self):
		queue = MaxPriorityQueue([Node(i) for i in [4, 3, 2, 1]])
		maximum = queue.extract_max()
		self.assertEqual(maximum.value, 4)
		self.assertIsNone(maximum.left)
		self.assertIsNone(maximum.right)

		maximum = queue.maximum()
		self.assertEqual(maximum.value, 3)
		self.assertEqual(maximum.left.value, 1)
		self.assertEqual(maximum.right.value, 2)


if __name__ == "__main__":
	main()
