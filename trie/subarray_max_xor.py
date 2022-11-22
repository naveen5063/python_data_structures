class Node:
    def __init__(self):
        self.c = []
        self.c.insert(0, None)
        self.c.insert(1, None)


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxval = max(A)
        maxpos = self.get_leftmax_bit(maxval)
        root = Node()
        for i in range(0, len(A)):
            self.insert(root, A[i], maxpos)

        ans = 0
        for i in range(0, len(A)):
            ans = max(ans, self.query(root, A[i], maxpos))

        return ans

    def get_leftmax_bit(self, maxval):
        pos = 0
        while maxval > 0:
            maxval = maxval >> 1
            pos += 1
        return pos

    def insert(self, root, val, maxpos):
        for i in range(maxpos, -1, -1):
            e = self.checkbit(val, i)
            if root.c[e] is None:
                root.c[e] = Node()
                root = root.c[e]
            else:
                root = root.c[e]

    def query(self, root, val, b):
        ans = 0
        for i in range(b, -1, -1):
            e = self.checkbit(val, i)
            print("root.c[1 - e]", root.c[1 - e])
            if root.c[1 - e] != None:
                ans += 1 << i
                root = root.c[1 - e]
            else:
                root = root.c[e]
        return ans

    def checkbit(self, val, i):
        return (val >> i) & 1 == 1


A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
s = Solution()
print(s.solve(A))
