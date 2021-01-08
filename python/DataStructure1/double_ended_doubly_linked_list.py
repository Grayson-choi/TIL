# Doubly Linked
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.previous = None

	def set_next(self, node):
		self.next = node

	def set_previous(self, node):
		self.previous = node

# Double Ended Doubly Linked List
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def set_head(self, node):
		self.head = node

	def set_tail(self, node):
		self.tail = node

	def is_empty(self):
		return self.head == None

	def add_front(self, value):

		new_node = Node(value)
		
		if self.is_empty():
			self.set_head(new_node)
			self.set_tail(new_node)
		else:
			new_node.set_next(self.head)
			self.head.set_previous(new_node)
			self.set_head(new_node)

	def add_last(self, value):
		new_node = Node(value)

		if self.is_empty():
			self.set_head(new_node)
			self.set_tail(new_node)
		else:
			new_node.set_previous(self.tail)
			self.tail.set_next(new_node)
			self.set_tail(new_node)


	def add_after(self, target_value, new_value):
		new_node = Node(new_value)
		iterator = self.head
		while (iterator.value != target_value):
			iterator = iterator.next

		iterator.next.set_previous(new_node)

		new_node.set_next(iterator.next)

		new_node.set_previous(iterator)

		iterator.set_next(new_node)

	def delete_first(self):
		self.set_head(self.head.next)

	def delete_last(self):
		self.set_tail(self.tail.previous)
		self.tail.set_next(None)

	def print_list(self):
		iterator = self.head
		while(iterator):
			print(iterator.value, end=' ')
			iterator = iterator.next


dll = DoublyLinkedList()



dll.add_front(5)
dll.add_front(1)
dll.add_last(999)
dll.delete_last()
dll.add_front(3)
dll.add_front(11)
dll.add_front(61)
dll.delete_last()
dll.add_front(2)
dll.add_last(599)

dll.print_list()


