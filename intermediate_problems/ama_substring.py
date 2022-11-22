class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        for i in range(0, len(A)):
            if A[i] in ["A", "E", "I", "O", "U"]:
                count = count + (len(A) - i)
                print(count)
                count = count % 10003
                print(count)
        return count

A = "ABEC"
s = Solution()
print(s.solve(A))