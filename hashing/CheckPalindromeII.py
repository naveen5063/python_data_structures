class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq_map = {}
        for i in range(len(A)):
            if A[i] in freq_map:
                freq_map[A[i]] += 1
            else:
                freq_map[A[i]] = 1

        count = 0
        for j in freq_map:
            if freq_map[j] % 2 != 0:
                count += 1

        if count > 1:
            return 0
        return 1

A = "abcde"
#A = "abbaee"

s = Solution()
print(s.solve(A))