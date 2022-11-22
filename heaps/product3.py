import heapq

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        pq = []
        ans = []
        for i in range(0, len(A)):
            print("A[i]", i, A[i])
            heapq.heappush(pq, -A[i])
            if i < 2:
                ans.append(-1)
            else:
                print("pq bf", pq)
                x = heapq.heappop(pq)
                y = heapq.heappop(pq)
                z = heapq.heappop(pq)
                print("pq", pq)
                prod = x * y * z
                print("ans", ans, prod)
                ans.append(-prod)
                print(x,y,z)
                heapq.heappush(pq, x)
                heapq.heappush(pq, y)
                #heapq.heappush(pq, z)
                print("pq af", pq)
        return ans

A = [1, 2, 3, 4, 5]
s = Solution()
print(s.solve(A))
