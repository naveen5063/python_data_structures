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

    def delete_at_pos(self, position):
        print("position", position, self.size)
        if position >= self.size or position < 0:
            return

        if position == 0:
            self.head = self.head.next
            self.size -= 1
            return

        pos = 0
        current_node = self.head
        print("current_node", current_node.val)
        while current_node.next:
            if pos == position - 1:
                current_node.next = current_node.next.next
                self.size -= 1
                return
            else:
                current_node = current_node.next
                pos += 1

    def get_size(self):
        size = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            size += 1
        return size

    def del_mid_ele(self):
        size = self.get_size()
        mid = int(size / 2)
        pos = 0
        current_node = self.head
        while current_node.next and pos < mid - 1:
            current_node = current_node.next
            pos += 1
        current_node.next = current_node.next.next

    def print_mid(self):
        size = self.get_size()
        mid = int(size / 2)
        pos = 0
        current_node = self.head
        while current_node.next and pos < mid:
            current_node = current_node.next
            pos += 1
        return current_node.val

    def print_ll(self):
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def reverse_list(self):
        print("rev ll", self.print_linked_lst(self.head))
        original_list = self.head
        reverse_list = None
        while original_list is not None:
            tmp = original_list
            original_list = original_list.next
            tmp.next = reverse_list
            reverse_list = tmp
        print("rev ll", self.print_linked_lst(self.head))
        return reverse_list

    def reverse_bw_list(self, start, end):
        print("start, end", start, end)
        print("self.head", self.head)
        original_list = self.head
        reverse_list = None
        pos = 0
        print("original_list", original_list.next)
        print("ll", self.print_linked_lst(original_list))
        while original_list is not None and pos < start - 1:
            original_list = original_list.next
            pos += 1
        print("pos", pos)
        print("original_list", original_list)
        original_bf_start = original_list

        print("original_list", original_list)
        while original_list is not None and pos <= end:
            print("original_list", original_list)
            tmp = original_list
            original_list = original_list.next
            tmp.next = reverse_list
            reverse_list = tmp
        print("reverse_list", reverse_list)
        print(self.print_linked_lst(reverse_list))
        end_list = reverse_list.next
        reverse_list.next = end_list
        original_bf_start.next = reverse_list

        return original_bf_start

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


insert_node(0, 10)
insert_node(1, 20)
insert_node(2, 30)
insert_node(2, 25)
insert_node(3, 35)
print(ll.get_size())
print(ll.print_mid())
# insert_node(5, 35)
# delete_node(3)
print_ll()

print("rev", ll.print_linked_lst(ll.reverse_list()))
print(ll.print_linked_lst(ll.reverse_bw_list(2, 3)))
