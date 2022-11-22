class DLL:

    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    # @return an integer
    def get(self, key):
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]
        if node.next is not None:
            self.remove(node)
            self.insertAtback(node)

        return node.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        node = DLL(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.cache[key] = node
            return

        if key not in self.cache.keys():
            if len(self.cache) == self.capacity:
                delnode = self.head
                if self.head.next == None and self.head.prev == None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
                print("self.cache", self.cache)
                print("self.cache len", len(self.cache))
                # print("delnode", delnode.key, delnode.val)
                self.cache.pop(delnode.key)
                # del self.cache[delnode.key]
                self.cache[key] = node
                self.insertAtback(node)

            else:
                self.insertAtback(node)
                self.cache[key] = node

        else:
            d1 = self.cache[key]
            d1.val = value
            if d1.next is not None:
                self.remove(d1)
                # del self.cache[d1.key]
                # self.cache[key] = node
                self.insertAtback(d1)

    def removeheadnode(self):
        deletenode = self.head
        if self.head.next == None and self.head.prev == None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return deletenode

    def remove(self, node):
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
            return
        if self.head == node:
            self.head == self.head.next
            self.head.prev = None
            return
        prevnode = node.prev
        nextnode = node.next
        nextnode.prev = prevnode
        if prevnode is not None:
            prevnode.next = nextnode

    def insertAtback(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node


# l1 = LRUCache(1)
# l1.set(2, 1)
# print(l1.get(2))
# l1.set(3, 2)
# print(l1.get(2))
# print(l1.get(3))

# l1 = LRUCache(1)
# print("set 2, 1")
# l1.set(2, 1)
# print("set 2, 2")
# l1.set(2, 2)
# # print("get 2")
# print("get 2", l1.get(2))
# print("set 1, 1")
# l1.set(1, 1)
# print("set 4, 1")
# l1.set(4, 1)
# print("get 2")
# print("get 2", l1.get(2))

operations = "S 5 13 S 9 6 S 4 1 G 4 S 6 1 S 8 11 G 13 G 1 S 12 12 G 10 S 15 13 S 2 13 S 7 5 S 10 3 G 6 G 10 S 15 14 S 5 12 G 5 G 7 G 15 G 5 G 6 G 10 S 7 13 G 14 S 8 9 G 4 S 6 11 G 9 S 6 12 G 3"
setoperation = 2
getoperation = 1
count = 0
l1 = LRUCache(4)
print("len(operations)", operations)
while count < len(operations):
    if operations[count] == "S":
        print("{operations[count + 2]", {operations[count + 2]})
        print("{operations[count + 3]", {operations[count + 3]})
        val = f'l1.set({operations[count + 2]}, {operations[count + 3]})'
        print("val", val)
        exec(val)
        count += setoperation + 1
    if operations[count] == "G":
        val = f'l1.set({operations[count + 2]})'
        exec(val)
        count += getoperation + 1
