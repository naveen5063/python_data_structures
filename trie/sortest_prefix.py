class Node:
    def __init__(self):
        self.hm_ref = {}
        self.hm_freq = {}
        self.isEnd = False


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A):
        spellcheckres = []
        node = Node()
        for val in A:
            self.add(val, node)

        for val in A:
            spellcheckres.append(self.find(val, node))
        return spellcheckres

    def add(self, val, node):
        charlen = len(val)
        for i in range(0, charlen):
            char = val[i]
            if not char in node.hm_ref.keys():
                tmpnode = Node()
                node.hm_freq[char] = 1
                node.hm_ref[char] = tmpnode
                node = node.hm_ref[char]
            else:
                node.hm_freq[char] += 1
                node = node.hm_ref[char]
        node.isEnd = True

    def find(self, val, node):
        res = []
        charlen = len(val)
        for i in range(0, charlen):
            char = val[i]
            if node.hm_freq[char] <= 1:
                res.append(char)
                return "".join(res)
                break
            else:
                res.append(char)
            node = node.hm_ref[char]
        return "".join(res)


A = ["hat", "cat", "rat"]
B = ["cat", "ball"]

# A = [ "tape", "bcci" ]
# B = [ "table", "cci" ]

A = ["zebra", "dog", "duck", "dove"]
s = Solution()
print(s.solve(A))
