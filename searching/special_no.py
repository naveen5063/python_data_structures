class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arrlen = len(A)
        low = 0
        high = arrlen
        ans = 0
        while low <= high:
            mid = int((low + high) / 2)
            maxsum = self.getmax_subarr_sum(A, arrlen, mid)
            if maxsum <= B:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def getmax_subarr_sum(self, A, arrlen, mid):
        sum = 0
        for i in range(0, mid):
            sum += A[i]
        start = 1
        end = mid
        ans = sum
        while start <= arrlen - mid:
            #print("start - 1", end)
            sum = sum - A[start - 1] + A[end]
            #print("ssum", sum)
            ans = max(ans, sum)
            start += 1
            end += 1
        return ans


A = [3, 2, 5, 4, 6, 3, 7, 2]
B = 10
# A = [1, 2, 3, 4, 5]
# B = 10
s = Solution()
print(s.solve(A, B))
