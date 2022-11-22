class Node:
    def __init__(self):
        self.hm = {}
        self.isEnd = False


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        spellcheckres = []
        node = Node()
        for val in A:
            self.add(val, node)

        for val in B:
            if self.find(val, node):
                spellcheckres.append(1)
            else:
                spellcheckres.append(0)
        return spellcheckres

    def add(self, val, node):
        charlen = len(val)
        for i in range(0, charlen):
            char = val[i]
            if not char in node.hm.keys():
                tmpnode = Node()
                node.hm[char] = tmpnode
                node = node.hm[char]
            else:
                node = node.hm[char]
        node.isEnd = True

    def find(self, val, node):
        charlen = len(val)
        for i in range(0, charlen):
            char = val[i]
            print("char", char)
            if char in node.hm.keys():
                print("node.hm.keys()", node.hm.keys())
                node = node.hm[char]
            else:
                return False
        return node.isEnd


A = ["hat", "cat", "rat"]
B = ["cat", "ball"]

A = [ "tape", "bcci" ]
B = [ "table", "cci" ]
s = Solution()
print(s.solve(A, B))
