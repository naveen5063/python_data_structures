from heapq import heappop, heappush, heapify


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Creating empty heap
        res = []
        s = 0
        maxheap = []
        minheap = []
        heapify(maxheap)
        heappush(maxheap, -1 * A[0])
        heapify(minheap)
        arrlen = len(A)
        # print(maxheap[0])
        res.append(A[0])
        for i in range(1, len(A)):
            #print("print(maxheap[0])", maxheap[0])
            maxheapval = -1 * maxheap[0]
            #print("maxheapval", A[i], maxheapval)
            if A[i] < maxheapval:
                heappush(maxheap, -1 * A[i])
            else:
                heappush(minheap, A[i])

            if len(maxheap) < len(minheap):
                ele = heappop(minheap)
                #print("ele", ele)
                heappush(maxheap, -1 * ele)
            elif len(maxheap) - len(minheap) > 1:
                #print("aaa")
                ele = heappop(maxheap)
                heappush(minheap, -1 * ele)
            #s = i + 1
            #print("s % 2", s, s % 2)
            #if s % 2 == 0:
            if len(maxheap) > len(minheap):
                val = -1 * maxheap[0]
                res.append(val)
            elif len(minheap) > len(maxheap):
                val = minheap[0]
                res.append(val)
            else:
                res.append(-1 * maxheap[0])
            #print("--", maxheap, minheap)
            #print("res", res)
        return res


A = [1, 2, 5, 4, 3]
A = [ 32, 91, 86, 8, 4, 100, 98, 15, 79, 32, 4, 99 ]

s = Solution()
print(s.solve(A))
