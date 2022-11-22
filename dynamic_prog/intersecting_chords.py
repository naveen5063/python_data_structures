class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        mod = 10000000007
        chords = [-1 for i in range(A + 1)]
        chords[0] = 1
        for k in range(1, A + 1):
            i = k - 1
            j = 0
            nways = 0
            while i >= 0:
                nways += chords[i] * chords[j]
                i -= 1
                j += 1
            chords[k] = nways
        return chords[A] % mod


A = 1
A = 2
s = Solution()
print(s.chordCnt(A))
