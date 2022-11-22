class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # brute force N2
        # max_subarr_sum = A[0]
        # for i in range(0, len(A)):
        #     sum = 0
        #     arr = []
        #     for j in range(i, len(A)):
        #         sum += A[j]
        #         arr.append(A[j])
        #         if sum == B:
        #             return arr
        # return -1

        p1 = 0
        p2 = 0
        subsum = A[p1]
        val = [-1]
        while p1 < len(A) and p2 < len(A):
            if subsum == B:
                val = []
                for i in range(p1, p2+1):
                    val.append(A[i])
                return val
            elif subsum < B and p2 < len(A) - 1:
                p2 += 1
                subsum += A[p2]
            else:
                subsum -= A[p1]
                p1 += 1
        return val


A = [1, 2, 3, 4, 5]
B = 5
#
# A = [5, 10, 20, 100, 105]
# B = 110

s = Solution()
print(s.solve(A, B))
