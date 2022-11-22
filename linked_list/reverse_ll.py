class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_pos(self, position, value):

        # print("self.size", self.size, position)
        if position > self.size or position < 0:
            return

        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.size += 1
            return

        if position == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        pos = 0
        new_node = Node(value)
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

    def reverse(self, head, count):
        print("count", count)
        prev = None
        curr = head
        temp = curr.next
        while count > 0:
            print("curr", curr.val)
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count -= 1
        return prev, temp


    def reverse_bw_list(self, start, end):
        left_node_before = self.head
        left_node = None
        pos = 0
        print("start - 1", start - 1)
        while left_node_before.next and start > 0:
            left_node_before = left_node_before.next
            #pos += 1
        if start > 0:
            left_node = left_node_before.next
        else:
            left_node = self.head
        right_node, right_node_after = self.reverse(left_node, end - start + 1)
        if left_node_before.next is not None:
            left_node_before.next = right_node
        else:
            self.head = right_node
        left_node.next = right_node_after
        return self.head

    def print_ll(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def get_linked_list(self):
        return self.head

    def print_linked_lst(self, ll):
        nodes = []
        current_node = ll
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)


ll = Linked_list()


def insert_node(position, value):
    ll.insert_at_pos(position, value)
    # @param position, an integer
    # @param value, an integer


def delete_node(position):
    ll.delete_at_pos(position)
    # @param position, integer
    # @return an integer


def print_ll():
    print(ll.print_ll())
    # Output each element followed by a space


# insert_node(0, 10)
# insert_node(1, 20)
# insert_node(2, 30)
# insert_node(2, 25)
# insert_node(3, 35)
# print_ll()
# 10 20 25 30 35
# 10 20 30 25 35
insert_node(0, 83)
insert_node(1, 13)
insert_node(2, 21)
insert_node(3, 72)
#72 -> 21 -> 13 -> 83
print("rev", ll.print_linked_lst(ll.reverse_bw_list(0, 3)))
# print_ll()
