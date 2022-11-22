class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        #print(A[0][0])
        #print("len(A[0])", len(A[0]))
        ans = A[0][0]
        for st in range(0, len(A)):
            sum = [0] * len(A[0])
            for end in range(st, len(A)):
                print(st, end)
                for i in range(0, len(A[0])):
                    print("-mat-", A[end][i])
                    sum[i] += A[end][i]
                print(sum)
                ans = max(ans, self.maxSubArray(sum, len(A[0])))
                print('ans', ans)

        # st = 0
        # ans = A[0][0]
        # sum = [0] * len(A[0])
        # for end in range(0, len(A)):
        #     print(st, end)
        #     for i in range(0, len(A[0])):
        #         #print(end, i)
        #         sum[i] += A[end][i]
        #     print(sum)
        #     ans = max(ans, self.maxSubArray(sum, len(A[0])))
        #     print('ans', ans)

    def maxSubArray(self, A, size):
        sum = 0
        max_subarr_sum = A[0]
        for i in range(0, size):
            sum += A[i]
            max_subarr_sum = max(sum, max_subarr_sum)
            if sum < 0:
                sum = 0
        return max_subarr_sum

A = [[-6, - 6],
[-29 ,- 8],
[3 ,- 8],
[-15, 2],
[25, 25],
[20 ,- 5]]

# A = [[2 , -4, 1, 3, -1, 2],
#      [1, 3, 2, -7 , 3, 3],
#      [0, -1, 1, 3, 4, -7],
#      [1, -1, -6, 4, -4, 6]]

# A = [
#   [-29, -19, -18, -2, 7, -11],
#   [17, 15, -11, -22, 24, -8],
#   [-22, 4, 3, 17, -8, 27],
#   [-25, -11, 23, 1, 8, 30],
#   [4, -2, -22, 17, 28, -27],
#   [2, -22, -11, -3, -16, -28],
#   [30, 2, 7, 16, 7, 22]
# ]
# A = [[-17, -2],
#      [20, 10]]

s = Solution()
s.solve(A)