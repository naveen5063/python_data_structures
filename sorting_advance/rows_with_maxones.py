class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        max1, row = 0, None
        rows, col = len(A), len(A[0]) - 1
        for i in range(rows):
            while A[i][col] == 1 and col >= 0:
                count += 1
                if count > max1:
                    max1 = count
                    row = i
                col -= 1
        return row


A = [[1, 0, 1],
     [0, 1, 0],
     [1, 0, 0]]

# A = [[0, 0, 0, 0],
#  [0, 1, 1, 1]]

s = Solution()
print("res", s.solve(A))