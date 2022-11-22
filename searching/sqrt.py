class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        ans = 0
        low = 1
        high = A
        while low <= high:
            mid = int((low + high) / 2)
            val = mid * mid
            if val == A:
                return mid
            if val > A:
                high = mid - 1
            if val < A:
                low = mid + 1
                ans = mid
        return ans


A = 9
s = Solution()
print(s.sqrt(A))
