from collections import defaultdict


class Node:
    def __init__(self):
        self.hmref = {}
        self.hmfreq = defaultdict(int)


class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        res = []
        root = Node()
        for i in range(0, len(A)):
            if A[i] == 0:
                self.insert(root, B[i])
            else:
                res.append(self.search(root, B[i]))
        return res

    def insert(self, root, val):
        chrlen = len(val)
        for i in range(0, chrlen):
            chr = val[i]
            if chr not in root.hmref.keys():
                chrref = Node()
                root.hmref[chr] = chrref
                root.hmfreq[chr] += 1
                root = root.hmref[chr]
            else:
                root.hmfreq[chr] += 1
                root = root.hmref[chr]

    def search(self, root, val):
        chrlen = len(val)
        for i in range(0, chrlen):
            chr = val[i]
            if chr not in root.hmref.keys():
                return 0
            else:
                if i == chrlen - 1:
                    return root.hmfreq.get(chr, 0)
                root = root.hmref[chr]


A = [0, 0, 1, 1]
B = ["hack", "hacker", "hac", "hak"]
A = [0, 1]
B = ["abcde", "abc"]
s = Solution()
print(s.solve(A, B))
