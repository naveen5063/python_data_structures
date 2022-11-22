class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A):
        i = 0
        j = 0
        max_len = 0
        char_set = set()
        while j < len(A):
            if A[j] not in char_set:
                char_set.add(A[j])
                j += 1
                max_len = max(max_len, len(char_set))
            else:
                char_set.remove(A[i])
                i += 1
        return max_len


A = ['a', 'b', 'a', 'c', 'e', 'a', 'f', 'f']
s = Solution()
print(s.solve(A))
