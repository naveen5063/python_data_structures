import array as arr
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        l1 = [0] * len(A)
        for val in A:
            l1[ord(val) - ord('a')] += 1

        for val in A:
            if l1[ord(val) - ord('a')] == 1:
                return val


A = "abadbc"
s = Solution()
print(s.solve(A))
