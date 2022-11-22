class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_count = {}
        for i in range(0, len(A)):
            if A[i] in freq_count:
                freq_count[A[i]] += 1
            else:
                freq_count[A[i]] = 1

        sorted_freq = sorted(freq_count.items(), key=lambda x: x[1])
        print(sorted_freq)

        x = len(sorted_freq)
        for val in sorted_freq:
            if val[1] <= B:
                B -= val[1]
                x -= 1

        print(x)
        return x


A = "aabcabbccd"
B = 3
s = Solution()
print(s.solve(A, B))
