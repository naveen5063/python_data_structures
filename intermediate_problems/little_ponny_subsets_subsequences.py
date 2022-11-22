class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        N = len(A)
        minval = A[0]
        minindx = 0
        for j in range(N - 1):
            val = ord(A[j])
            if val < ord(minval):
                minval = A[j]
                minindx = j

        secval = A[minindx + 1]
        secindx = minindx + 1
        for k in range(minindx + 1, N):
            val = ord(A[k])
            if val < ord(secval):
                secval = A[k]
                secindx = k

        if minindx < secindx:
            return minval + secval
        else:
            return secval + minval


A = "abcdsfhjagj"
A = "ksdjgha"
s = Solution()
print(s.solve(A))
