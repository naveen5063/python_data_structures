from typing import Optional


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def get_ll(self):
        return self.head

    def print_linked_lst(self, ll):
        nodes = []
        current_node = ll
        while current_node:
            nodes.append(str(current_node.val))
            current_node = current_node.next
        return " ".join(nodes)

    def mergeTwoLists(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


llist1 = linkedList()
llist1.insert_at_first(1)
llist1.insert_at_last(2)
llist1.insert_at_last(4)
l1 = llist1.get_ll()
print(llist1.print_linked_lst(l1))
print("------------------")
llist2 = linkedList()
llist2.insert_at_first(3)
llist2.insert_at_last(5)
llist2.insert_at_last(6)
l2 = llist2.get_ll()
print(llist2.print_linked_lst(l2))
llist3 = linkedList()
res = llist3.mergeTwoLists(l1, l2)
print(llist3.print_linked_lst(res))
#print("res", res)