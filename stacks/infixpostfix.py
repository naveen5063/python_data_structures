class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        hm = {}
        hm['^'] = 1
        hm['/'] = 2
        hm['*'] = 2
        hm['+'] = 3
        hm['-'] = 3
        stack = []
        ans = ""
        for i in range(0, len(A)):
            if A[i] not in hm.keys():
                ans += A[i]
            else:
                while stack > 0 and A[i] in hm.keys():






A = "x^y/(a*z)+b"
#"xy^az*/b+"
A = "1+3*4"
s = Solution()
s.solve(A)