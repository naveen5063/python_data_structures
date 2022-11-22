from heapq import heappop, heappush, heapify


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        minheap = []
        heapify(minheap)
        sum = 0
        for i in range(0, len(A)):
            if A[i] <= 0:
                heappush(minheap, abs(A[i]))
                B -= 1
            else:
                heappush(minheap, A[i])

        while B > 0 and len(minheap) > 0:
            val = heappop(minheap)
            if val >= 0:
                heappush(minheap, -abs(val))
            else:
                heappush(minheap, abs(val))
            B -= 1

        print("minheap", minheap)
        while len(minheap) > 0:
            val = heappop(minheap)
            sum += val

        return sum

# A = [24, -68, -29, -9, 84]
# B = 4
#
# A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
# # [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]
# B = 10
#
# A = [52, 35]
# B = 10

A = [ -20, 73, 89, -35, -20, 12, 25, -17, 93 ]
B = 3

s = Solution()
print(s.solve(A, B))
