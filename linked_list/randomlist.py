class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_first(self, ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            new_ele = Node(ele)
            new_ele.next = self.head
            self.head = new_ele

    def insert_at_last(self, ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            new_ele = Node(ele)
            currentnode = self.head
            while currentnode.next:
                currentnode = currentnode.next
            currentnode.next = new_ele

    def insert_at_pos(self, index, ele):
        pos = 0
        if self.head is None:
            self.head = Node(ele)
        else:
            newele = Node(ele)
            currentele = self.head
            while currentele.next and pos < index - 1:
                currentele = currentele.next
                pos += 1
            newele.next = currentele.next
            currentele.next = newele

    def delete_at_pos(self, index):
        if self.head is None:
            return
        pos = 0
        current_ele = self.head
        if index == 0:
            self.head = self.head.next
        else:
            while current_ele.next and pos < index - 1:
                current_ele = current_ele.next
                pos += 1
            current_ele.next = current_ele.next.next

    def print_linked_lst(self, ll=None):
        if not ll:
            ll = self.head
        nodes = []
        current_node = ll
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def create_copy_inbw(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:
            tmp = current.next
            current.next = Node(current.val)
            current = current.next
            current.next = tmp
            current = current.next
        return self.head

    def generate_random_for_copy(self):
        if self.head is None:
            return None
        t1 = self.head
        t2 = self.head.next
        while t1 is not None:
            if t1.random is not None:
                t2.random = t1.random
            else:
                t2.random = None
            t1 = t1.next.next
            if t2.next is not None:
                t2 = t2.next.next

    def generate_deep_cp(self):
        if self.head is None:
            return None
        t1 = self.head
        t2 = self.head.next
        while t1 is not None:
            t1.next = t2.next
            t1 = t1.next
            if t1 is not None:
                t2.next = t1.next
            t2 = t2.next
        return self.head


llist = linkedList()
llist.insert_at_first(3)
llist.insert_at_first(4)
llist.insert_at_last(5)
llist.insert_at_last(8)
print(llist.print_linked_lst())
res = llist.create_copy_inbw()
llist.generate_random_for_copy()
#print("res", llist.print_linked_lst(res))
