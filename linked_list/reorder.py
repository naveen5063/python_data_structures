class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class Linked_list():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_pos(self, position, value):

        #print("self.size", self.size, position)
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

    def print_linked_list(self, ll):
        nodes = []
        current_node = ll
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def print_ll(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def reorder(self):
        #print("original", self.print_linked_list(self.head))
        # finding mid
        s = self.head
        f = self.head
        l1 = s
        while f and f.next:
            s = s.next
            f = f.next.next

        #reverse list
        l2 = s.next
        s.next = None
        print("l2", self.print_linked_list(l2))
        # rev_l2 = self.reverse(l2)
        # print("l1", self.print_linked_list(l1))
        # print("rev", self.print_linked_list(rev_l2))
        # l3 = l1  # point to head
        # l = l1  # new ll
        # l1 = l1.next # traverse l1
        # flag = 2
        # while rev_l2 is not None:
        #     if flag == 1:
        #         l.next = l1
        #         l1 = l1.next
        #         l = l.next
        #         flag = 2
        #     else:
        #         l.next = rev_l2
        #         rev_l2 = rev_l2.next
        #         l = l.next
        #         flag = 1
        # if l1 is not None:
        #     l.next = l1
        # #print("l3", self.print_linked_list(l3))

    def reverse(self, head):
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev


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


# insert_node(0, 1)
# insert_node(1, 2)
# insert_node(2, 3)
# insert_node(3, 4)
# #insert_node(4, 5)

# delete_node(3)

data = [90,94,25,51,45,29,55,63,48,27,72,10,36,68,16,20,31,7,95,70,89,23,22,9,74,71,35,5,80,11,49,92,69,6,37,84,78,28,43,64,96,57,83,13,73,97,75,59,53,52,19,18,98,12,81,24,15,60,79,34,1,54,93,65,44,4,87,14,67,26,30,77,58,85,33,21,46,82,76,88,66,101,61,47,8]
for i in range(0, len(data)):
    insert_node(i, data[i])

print_ll()
ll.reorder()
print_ll()