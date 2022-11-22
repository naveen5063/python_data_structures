class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def __init__(self):
        self.res = []

    def subsets(self, A):
        A.sort()
        self.res.append([])
        self.print_subset(A, [], len(A), 0)
        unique_data = [list(x) for x in set(tuple(x) for x in self.res)]
        unique_data.sort()
        return unique_data

    def print_subset(self, A, l, N, i):
        if i == N:
            return

        l.append(A[i])
        self.res.append(l[:])
        self.print_subset(A, l, N, i + 1)
        l.pop()
        self.print_subset(A, l, N, i + 1)


A = [1, 2, 3]
A = [1, 2, 2]
s = Solution()
print(s.subsets(A))

# [
#  []
#  [1]
#  [1, 2]
#  [1, 2, 3]
#  [1, 3]
#  [2]
#  [2, 3]
#  [3]
# ]
