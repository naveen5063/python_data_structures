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
                self.cache.pop(delnode.key)
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
			#node.prev = None
            #node.next = None
            return
        if self.head == node:
            self.head = self.head.next
            self.head.prev = None
			#node.prev = None
            #node.next = None
            return
        prevnode = node.prev
        nextnode = node.next
        nextnode.prev = prevnode
		#node.prev = None
        #node.next = None
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


if __name__ == "__main__":
    # l1 = LRUCache(2)
    # l1.set(1, 10)
    # l1.set(5, 12)
    # l1.set(6, 20)
    # print(l1.get(1))

    l1 = LRUCache(1)
    print("set 2, 1")
    l1.set(2, 1)
    print("set 2, 2")
    l1.set(2, 2)
    #print("get 2")
    print("get 2", l1.get(2))
    print("set 1, 1")
    l1.set(1, 1)
    print("set 4, 1")
    l1.set(4, 1)
    print("get 2")
    print("get 2", l1.get(2))
