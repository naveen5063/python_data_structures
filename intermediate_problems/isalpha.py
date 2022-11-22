class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):
        for i in range(0, len(A)):
            if not A[i].isalnum():
                return 0
        return 1



A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y']
A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
s = Solution()
print(s.solve(A))