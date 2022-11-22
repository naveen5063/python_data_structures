from heapq import heappop, heappush, heapify


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pairs = []
        minheap = []
        heapify(minheap)
        count = 1
        for i in range(len(A)):
            pairs.append([A[i], B[i]])
        pairs.sort()

        for j in range(len(A)):
            pair = pairs[j]
            time, profit = pair[0], pair[1]
            if time > len(minheap):
                heappush(minheap, profit)
                print("minheap[0]", minheap[0])



            elif profit > minheap[0]:
                heappop(minheap)
                heappush(minheap, profit)

        ans = 0
        while len(minheap) > 0:
            ans += heappop(minheap)
        return ans


A = [1, 3, 2, 3, 3]
B = [5, 6, 1, 3, 9]

A = [3, 8, 7, 5]
B = [3, 1, 7, 19]
s = Solution()
print(s.solve(A, B))
