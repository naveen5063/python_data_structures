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


    def sum_linked_list(self, l1 , l2):
        res = []
        currentl1 = l1
        currentl2 = l2
        carry = 0

        while currentl1 is not None or currentl2 is not None:
            l1data = 0 if currentl1 is None else currentl1.val
            l2data = 0 if currentl2 is None else currentl2.val
            sum = carry + l1data + l2data
            print("sum", sum)
            carry = int(sum / 10) if sum >= 10 else 0
            print("carry", carry)
            sum = sum if sum < 10 else sum % 10
            res.append(sum)
            if currentl1 is not None:
                currentl1 = currentl1.next
            if currentl2 is not None:
                currentl2 = currentl2.next
        #sum = carry + l1data + l2data
        #res.append(sum)
        print("res ", res)





llist1 = linkedList()
llist1.insert_at_first(3)
llist1.insert_at_last(10)
llist1.insert_at_last(5)
llist1.printlinkedlist()
print("------------------")
llist2 = linkedList()
llist2.insert_at_first(2)
llist2.insert_at_last(10)
llist2.printlinkedlist()
print("------------------")
reslist = linkedList()
reslist.sum_linked_list(llist1.head, llist2.head)

