class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = A[0]
        print(ans)
        for i in range(1, len(A)-1):
            print(A[i])
            ans = A[i] & ans
            #print(ans)
        return ans


A = [10, 20, 15, 4, 14]
s = Solution()
print(s.solve(A))