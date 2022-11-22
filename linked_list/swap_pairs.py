class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_at_first(self, ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            new_ele = Node(ele)
            new_ele.next = self.head
            self.head = new_ele
        self.count += 1

    def insert_at_last(self, ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            new_ele = Node(ele)
            currentnode = self.head
            while currentnode.next:
                currentnode = currentnode.next
            currentnode.next = new_ele
        self.count += 1

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
        self.count -= 1

    def printlinkedlist(self):
        if self.head is None:
            return None
        else:
            currentele = self.head
            while currentele.next:
                print("currentele", currentele.val)
                currentele = currentele.next
            print("currentele", currentele.val)
            print("count", self.count)

    def swap_pairs(self):
        if self.head is None:
            return None
        if self.count > 1:
            current_node = self.head
            counter = 1
            while current_node is not None and counter < self.count:
                if current_node.next:
                    tmp = current_node.val
                    current_node.val = current_node.next.val
                    current_node.next.val = tmp
                    current_node = current_node.next.next
                else:
                    return



llist1 = linkedList()
llist1.insert_at_first(3)
llist1.insert_at_last(10)
llist1.insert_at_last(5)
llist1.insert_at_last(4)
llist1.insert_at_last(8)
llist1.insert_at_last(12)
llist1.printlinkedlist()
print("------------------")
llist1.swap_pairs()
print("------------------")
llist1.printlinkedlist()
print("------------------")
