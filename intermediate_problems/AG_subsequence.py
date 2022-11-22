class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        res = 0
        count = 0
        for i in range(len(A) -1, -1, -1):
            if A[i] == "G":
                count += 1
            elif A[i] == "A":
                res += count
        return res



A = "ABCGAG"
s = Solution()
print(s.solve(A))