class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, position, value):
        # @param position, an integer
        # @param value, an integer
        if position == 1:
            cur_node = Node(value)
            cur_node.next = llist.head
            llist.head = cur_node
        else:
            current = llist.head
            current_pos = 1
            while current:
                if current_pos == position -1:
                    new_node = Node(value)
                    new_node.next = current.next
                    current.next = new_node
                    return
                else:
                    current = current.next
                    current_pos += 1

    def delete_node(self, position):
        # @param position, integer
        # @return an integer
        if position == 1:
            llist.head = llist.head.next
        else:
            current = llist.head
            current_pos = 1
            while current.next:
                if current_pos == position-1:
                    current.next = current.next.next
                    return
                else:
                    current = current.next
                    current_pos += 1
            return

    def print_ll(self):
        # Output each element followed by a space
        if llist.head == None:
            return None
        else:
            current = llist.head
            while current.next:
                print(current.val, end=" ")
                current = current.next
            print(current.val)

def insert_node(position, value):
    llist.insert_node(position, value)


def delete_node(position):
    llist.delete_node(position)


def print_ll():
    llist.print_ll()

# i 1 23
# i 2 24
# p
# d 1
# p
llist = LinkedList()
#print(llist)
insert_node(1, 23)
insert_node(2, 24)
#print_ll()
delete_node(1)
#print_ll()
