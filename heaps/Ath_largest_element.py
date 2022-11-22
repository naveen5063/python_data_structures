from heapq import heappop, heappush, heapify


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        minheap = []
        res = []
        heapify(minheap)
        for i in range(0, A):
            heappush(minheap, B[i])
            if i != A - 1:
                res.append(-1)

        print(res, minheap)
        res.append(minheap[0])
        print(res, minheap)

        for i in range(A, len(B)):
            heappop(minheap)
            heappush(minheap, B[i])
            res.append(minheap[0])

        print(res, minheap)


A = 4
B = [1, 2, 3, 4, 5, 6]
# A = 2
# B = [15, 20, 99, 1]

s = Solution()
print(s.solve(A, B))
