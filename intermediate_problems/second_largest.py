from heapq import heappop, heappush, heapify


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxheap = []
        heapify(maxheap)
        for i in range(0, len(A)):
            heappush(maxheap, -1 * A[i])
        if len(maxheap) > 1:
            second_max = 0
            for i in range(0, 2):
                second_max = -1 * (heappop(maxheap))
            return second_max
        return A[0]


A = [2, 1, 2]

A = [2]

s = Solution()
print(s.solve(A))
