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
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list3 = list1
            temp = list1
            list1 = list1.next
        elif list2.val < list1.val:
            list3 = list2
            temp = list2
            list2 = list2.next
        else:
            list3 = list1
            temp = list1
            list1 = list1.next
            #list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
                #print("ll", self.print_linked_lst(list3))
            elif list2.val < list1.val:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
                #print("ll", self.print_linked_lst(list3))
            else:
                temp.next = list1
                temp = temp.next
                temp.next = list2
                list1 = list1.next
                list2 = list2.next
                #temp = temp.next

        #print("ll", self.print_linked_lst(list3))

        if list1 is None:
            temp.next = list2
        if list2 is None:
            temp.next = list1

        return list3


llist1 = linkedList()
llist1.insert_at_first(1)
llist1.insert_at_last(2)
llist1.insert_at_last(4)
l1 = llist1.get_ll()
print(llist1.print_linked_lst(l1))
print("------------------")
llist2 = linkedList()
llist2.insert_at_first(1)
llist2.insert_at_last(3)
llist2.insert_at_last(4)
l2 = llist2.get_ll()
print(llist2.print_linked_lst(l2))
llist3 = linkedList()
res = llist3.mergeTwoLists(l1, l2)
print(llist3.print_linked_lst(res))
#print("res", res)