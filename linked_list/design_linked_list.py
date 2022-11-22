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


    def printlinkedlist(self):
        if self.head is None:
            return None
        else:
            currentele = self.head
            while currentele.next:
                print("currentele", currentele.val)
                currentele = currentele.next
            print("currentele", currentele.val)


llist = linkedList()
llist.insert_at_first(3)
llist.insert_at_first(4)
llist.insert_at_last(5)
llist.insert_at_last(8)
llist.insert_at_pos(4, 10)
llist.delete_at_pos(1)
llist.printlinkedlist()