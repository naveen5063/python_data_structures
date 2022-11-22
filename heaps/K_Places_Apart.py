from heapq import heappop, heappush, heapify
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []
        minheap = []
        heapify(minheap)
        for i in range(0, len(A)):
            heappush(minheap, A[i])
        while minheap:
            res.append(heappop(minheap))
        print(res)



A = [1, 40, 2, 3]
B = 2
# A = [2, 1, 17, 10, 21, 95]
# B = 1
s = Solution()
s.solve(A, B)