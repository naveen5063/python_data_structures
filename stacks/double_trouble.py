class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s = []
        flag = False
        for i in range(0, len(A)):
            while len(s) > 0 and A[i] is s[-1]:
                s.pop()
                flag = True
            if not flag:
                s.append(A[i])
            else:
                flag = False
        return ''.join(s)
A = "abccbc"
#"ac"
s = Solution()
print(s.solve(A))