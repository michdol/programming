from unittest import TestCase, main as unittest_main

from unoptimized_linked_list import UnoptimizedLinkedList, Node


class LinkedListTest(TestCase):
	def create_simple_list(self):
		llist = UnoptimizedLinkedList()

		first = Node(1)
		second = Node(2)
		third = Node(3)
		llist.head = first
		llist.head.next = second
		second.next = third
		return llist, first, second, third

	def test_with_comment(self):
		# Start with the empty list
		llist = UnoptimizedLinkedList()

		llist.head = Node(1)
		second = Node(2)
		third = Node(3)

		''' 
		Three nodes have been created. 
		We have references to these three blocks as first, 
		second and third 

		llist.head        second              third 
			 |                |                  | 
			 |                |                  | 
		+----+------+     +----+------+     +----+------+ 
		| 1  | None |     | 2  | None |     |  3 | None | 
		+----+------+     +----+------+     +----+------+ 
		'''

		llist.head.next = second  # Link first node with second

		''' 
		Now next of first Node refers to second.  So they 
		both are linked. 

		llist.head        second              third 
			 |                |                  | 
			 |                |                  | 
		+----+------+     +----+------+     +----+------+ 
		| 1  |  o-------->| 2  | null |     |  3 | null | 
		+----+------+     +----+------+     +----+------+  
		'''

		second.next = third  # Link second node with the third node

		''' 
		Now next of second Node refers to third.  So all three 
		nodes are linked. 

		llist.head        second              third 
			 |                |                  | 
			 |                |                  | 
		+----+------+     +----+------+     +----+------+ 
		| 1  |  o-------->| 2  |  o-------->|  3 | null | 
		+----+------+     +----+------+     +----+------+  
		'''

	def test_create_linked_list(self):
		llist = UnoptimizedLinkedList()

		first = Node(1)
		second = Node(2)
		third = Node(3)

		llist.head = first

		llist.head.next = second

		second.next = third

		self.assertIs(llist.head, first)

		# Both point to the same node.
		self.assertIs(llist.head.next, second)
		self.assertIs(first.next, second)

		# Same here.
		self.assertIs(llist.head.next.next, third)
		self.assertIs(second.next, third)

	def test___str__(self):
		llist, first, second, third = self.create_simple_list()
		fourth = Node(4)
		third.next = fourth
		test_string = llist.__str__()
		expected_string = "Linked list <1, 2, 3, 4, ...>"
		self.assertEqual(test_string, expected_string)

		fifth = Node(5)
		fourth.next = fifth
		test_string = llist.__str__()
		expected_string = "Linked list <1, 2, 3, 4, ...>"
		self.assertEqual(test_string, expected_string)

	def test_prepend(self):
		llist, first, second, third = self.create_simple_list()
		llist.prepend(4)
		self.assertIs(llist.head.data, 4)

	def test_get_last_node(self):
		llist = UnoptimizedLinkedList()
		self.assertIsNone(llist.get_last_node())
		first = Node(1)
		llist.head = first
		self.assertIs(llist.get_last_node(), first)
		second = Node(2)
		llist.head = second
		self.assertIs(llist.get_last_node(), second)

	def test_append(self):
		llist, first, second, third = self.create_simple_list()
		llist.append(4)
		self.assertIs(third.next.data, 4)

	def test_append_empty_list(self):
		llist = UnoptimizedLinkedList()
		llist.append(1)
		self.assertEqual(llist.head.data, 1)

	def test_insert(self):
		llist, first, second, third = self.create_simple_list()
		llist.insert(llist.head, 5)
		self.assertEqual(llist.head.next.data, 5)
		second = llist.head.next
		self.assertEqual(second.next.data, 2)
		text_string = llist.__str__()
		expected_string = "Linked list <1, 5, 2, 3, ...>"
		self.assertEqual(text_string, expected_string)

	def test_insert_empty_list(self):
		llist = UnoptimizedLinkedList()
		node = Node(1)
		with self.assertRaises(ValueError) as e:
			llist.insert(node, 2)
			self.assertEqual(e.exception.args[0], "Cannot insert while the list is empty")

	def test_insert_prev_node_is_none(self):
		llist = UnoptimizedLinkedList()
		llist.head = Node(2)
		with self.assertRaises(ValueError) as e:
			llist.insert(None, 1)
		self.assertEqual(e.exception.args[0], "Previous node must be Node")

	def test_get_prev_node(self):
		llist, first, second, third = self.create_simple_list()
		self.assertIsNone(llist.get_prev_node(first))
		self.assertIs(llist.get_prev_node(second), first)
		self.assertIs(llist.get_prev_node(third), second)

	def test_get_prev_node_param_is_none(self):
		llist = UnoptimizedLinkedList()
		llist.head = Node(1)
		with self.assertRaises(ValueError) as e:
			llist.get_prev_node(None)
		self.assertEqual(e.exception.args[0], "node argument must be Node")

	def test_get_prev_node_empty_list(self):
		llist = UnoptimizedLinkedList()
		node = Node(1)
		with self.assertRaises(ValueError) as e:
			llist.get_prev_node(node)
		self.assertEqual(e.exception.args[0], "the list is empty")

	def test_delete_first_node(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete(1)
		self.assertIs(llist.head, second)
		self.assertIs(llist.head.next, third)
		text_string = llist.__str__()
		expected_string = "Linked list <2, 3, ...>"
		self.assertEqual(text_string, expected_string)

	def test_delete_first_node_one_element_list(self):
		llist = UnoptimizedLinkedList()
		llist.append(1)
		llist.delete(1)
		self.assertIsNone(llist.head)
		text_string = llist.__str__()
		expected_string = "Linked list <, ...>"
		self.assertEqual(text_string, expected_string)

	def test_delete_second_node(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete(2)
		self.assertIs(llist.head, first)
		self.assertIs(llist.head.next, third)
		text_string = llist.__str__()
		expected_string = "Linked list <1, 3, ...>"
		self.assertEqual(text_string, expected_string)

	def test_delete_last_node(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete(3)
		self.assertIsNone(second.next)
		text_string = llist.__str__()
		expected_string = "Linked list <1, 2, ...>"
		self.assertEqual(text_string, expected_string)

	def test_delete_value_not_present_in_the_list(self):
		llist, first, second, third = self.create_simple_list()
		with self.assertRaises(ValueError) as e:
			llist.delete(4)
		self.assertEqual(e.exception.args[0], "4 not present in the list")

	def test_delete_at_index_first_element(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete_at_index(0)
		self.assertIs(llist.head, second)

	def test_delete_at_index_middle_element(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete_at_index(1)
		self.assertIs(llist.head.next, third)

	def test_delete_at_index_last_element(self):
		llist, first, second, third = self.create_simple_list()
		llist.delete_at_index(2)
		self.assertIsNone(llist.head.next.next)

	def test_delete_at_index_out_of_range(self):
		llist, first, second, third = self.create_simple_list()
		with self.assertRaises(IndexError) as e:
			# Delete fourth element.
			llist.delete_at_index(3)
		self.assertEqual(e.exception.args[0], "list index out of range")

		with self.assertRaises(IndexError) as e:
			# Delete fifth element.
			llist.delete_at_index(4)
		self.assertEqual(e.exception.args[0], "list index out of range")

	def test_delete_at_index_from_empty_list(self):
		# Empty list
		llist = UnoptimizedLinkedList()
		with self.assertRaises(IndexError) as e:
			llist.delete_at_index(0)
		self.assertEqual(e.exception.args[0], "\delete from empty list")

	def test_is_iterable(self):
		llist = UnoptimizedLinkedList()
		self.assertTrue(llist.is_iterable([]))
		self.assertTrue(llist.is_iterable(()))
		self.assertTrue(llist.is_iterable(''))
		self.assertFalse(llist.is_iterable(1))

	def test_convert_from_list(self):
		input = [1, 2, 3]
		llist = UnoptimizedLinkedList(iterable=input)
		self.assertEqual(llist.head.data, 1)
		self.assertEqual(llist.head.next.data, 2)
		self.assertEqual(llist.head.next.next.data, 3)

	def test_convert_from_empty_list(self):
		llist = UnoptimizedLinkedList(iterable=[])
		self.assertIsNone(llist.head)

	def test_convert_from_tuple(self):
		input = (1, 2, 3)
		llist = UnoptimizedLinkedList(iterable=input)
		self.assertEqual(llist.head.data, 1)
		self.assertEqual(llist.head.next.data, 2)
		self.assertEqual(llist.head.next.next.data, 3)
		self.assertIsNone(llist.head.next.next.next)

	def test_convert_from_one_element_tuple(self):
		input = (1,)
		llist = UnoptimizedLinkedList(iterable=input)
		self.assertEqual(llist.head.data, 1)
		self.assertIsNone(llist.head.next)

	def test_convert_from_dict(self):
		a = {'a': 1, 'b': 2}
		llist = UnoptimizedLinkedList(iterable=a)
		self.assertEqual(llist.head.data, 'a')
		self.assertEqual(llist.head.next.data, 'b')

	def test_iterate(self):
		llist, first, second, third = self.create_simple_list()
		for idx, elem in enumerate(llist):
			if idx == 0:
				self.assertIs(elem, first)
			elif idx == 1:
				self.assertIs(elem, second)
			elif idx == 2:
				self.assertIs(elem, third)

	def test_iterate_empty_list(self):
		llist = UnoptimizedLinkedList()
		with self.assertRaises(StopIteration):
			next(llist)

	def test_len(self):
		llist = UnoptimizedLinkedList()
		self.assertEqual(len(llist), 0)
		node = Node(1)
		llist.head = node
		self.assertEqual(len(llist), 1)
		llist, first, second, third = self.create_simple_list()
		self.assertEqual(len(llist), 3)


if __name__ == "__main__":
	unittest_main()
