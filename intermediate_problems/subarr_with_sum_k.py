class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        curr_sum = A[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > B and start < i - 1:
                curr_sum = curr_sum - A[start]
                start += 1
            if curr_sum == B:
                return A[start:i]

            if i < n:
                curr_sum = curr_sum + A[i]
            i += 1
        return [-1]


        # for i in range(0, len(A)):
        #     sum = 0
        #     arr = []
        #     for j in range(i, len(A)):
        #         sum += A[j]
        #         arr.append(A[j])
        #         print(arr)
        #         if sum == B:
        #             return arr
        # return -1

A = [1, 2, 3, 4, 5]
B = 5
# A = [5, 10, 20, 100, 105]
# B = 110
s = Solution()
print(s.solve(A, B))




