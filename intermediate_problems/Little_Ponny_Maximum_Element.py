class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = 0
        flag = False
        for i in range(0, len(A)):
            if A[i] == B:
                flag = True
        if flag:
            for i in range(0, len(A)):
                if A[i] > B:
                    count += 1
            return count
        return -1


A = [2, 4, 3, 1, 5]
B = 3

# A = [1, 4, 2]
# B = 3

s = Solution()
print(s.solve(A, B))
