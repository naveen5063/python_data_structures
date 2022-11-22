class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            ls = [0, 1]
            return ls
        p = list(self.grayCode(A - 1))
        x = len(p)
        print("x", x)
        ans = []
        for i in range(0, x):
            ans.append(p[i])
        for j in range(x - 1, -1, -1):
            val = p[j] + x
            ans.append(val)
        return ans


A = 2
# [0, 1, 3, 2]
# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].

s = Solution()
print(s.grayCode(A))
