class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxset(self, A):
        max_subarr = []
        new_arr = []
        max_sum = A[0]
        sum = 0
        for i in range(0, len(A)):
            if A[i] >= 0:
                sum += A[i]
                new_arr.append(A[i])
            else:
                sum = 0
                new_arr = []
            if max_sum < sum or max_sum == sum and len(new_arr) > len(max_subarr):
                max_subarr = new_arr
                max_sum = sum
        return max_subarr

A = [1, 2, 5, -7, 2, 3]
A = [ 0, 0, -1, 0 ]
#A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
s = Solution()
print(s.maxset(A))