class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = A - B
        return n
        # ans = 0
        # for i in range(1, B):
        #     if A % i == B % i:
        #         if i > ans:
        #             ans = i
        #         if i > A:
        #             return ans
        #             break
        # return ans



A = 1
B = 2
A = 5
B = 10

A = 7447727
B = 5671081

s = Solution()
print(s.solve(A, B))