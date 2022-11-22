#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def __init__(self):
		self.head = None
		self.size = 0

	def insert_at_pos(self, position, value):

		# print("self.size", self.size, position)
		if position > self.size or position < 0:
			return

		if self.head is None:
			new_node = ListNode(value)
			self.head = new_node
			self.size += 1
			return

		if position == 0:
			new_node = ListNode(value)
			new_node.next = self.head
			self.head = new_node
			self.size += 1
			return

		pos = 0
		new_node = ListNode(value)
		current_node = self.head
		while pos < position - 1 and current_node is not None:
			current_node = current_node.next
			pos += 1

		new_node.next = current_node.next
		current_node.next = new_node
		self.size += 1

	def get_size(self):
		size = 0
		current_node = self.head
		while current_node:
			current_node = current_node.next
			size += 1
		return size

	def reverse(self, head):
		if head == None:
			return None

		prev = None
		curr = head
		while curr.next is not None:
			tmp = curr.next
			curr.next = prev
			prev = curr
			curr = tmp
		return prev

	def divide_based_on_mid(self):
		val = self.get_size()
		mid = int(val + 1/2)
		l1 = self.head
		l1_head = l1
		l2 = None
		while mid > 0:
			l1 = l1.next
			mid -= 1
		l2 = l1.next
		l1.next = None


		rev_l2 = self.reverse(l2)
		while l1_head is not None and rev_l2 is not None:
			tmp = l1_head.next
			l1_head.next = rev_l2



	def reorderList(self, A):
		return A

	def print_ll(self):
		nodes = []
		current_node = self.head
		while current_node:
			nodes.append(str(current_node.val))
			current_node = current_node.next
		return " ".join(nodes)


ll = Solution()
def insert_node(position, value):
	ll.insert_at_pos(position, value)

def print_ll():
	print(ll.print_ll())

insert_node(0, 1)
insert_node(1, 2)
insert_node(2, 3)
insert_node(3, 4)
insert_node(4, 5)
insert_node(5, 6)
print(print_ll())

#A = [1, 2, 3, 4, 5]
#[1, 5, 2, 4, 3]