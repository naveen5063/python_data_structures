class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        freq = []
        final_freq = [0] * len(A)
        for i in range(0, len(A)):
            from_val = 0
            to_val = len(A) - 1
            if i - A[i] >= 1:
                from_val = i - A[i]
            if i + A[i] < len(A):
                to_val = i + A[i]
            freq.append([from_val, to_val])

        for j in range(0, len(freq)):
            for i in range(freq[j][0], freq[j][1]+1):
                final_freq[i] += 1
        return final_freq


A = [1, 0, 2 , 3, 2]
A = [1, 2, 3, 4, 5]
s = Solution()
s.solve(A)
