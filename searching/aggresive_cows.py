import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        low = self.get_min_distance(A)
        high = A[len(A) - 1] - A[0]
        print("low", low, high)
        ans = 0
        while low <= high:
            mid = int((low + high) / 2)
            if self.check(mid, A, len(A), B):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def get_min_distance(self, A):
        min_dist = sys.maxsize
        for i in range(0, len(A) - 1):
            adj_dist = A[i + 1] - A[i]
            print("adj_dist", adj_dist)
            min_dist = min(adj_dist, min_dist)
            print(min_dist)
        return min_dist

    def check(self, mid, C, param, A):
        last_updated = C[0]
        count = 1
        print("c check", C, mid)
        for i in range(1, param):
            if (C[i] - last_updated) >= mid:
                last_updated = C[i]
                count += 1
                if count == A:
                    return True
        return False


A = [1, 2, 3, 4, 5]
B = 3

A = [ 5, 17, 100, 11 ]
B = 2

# A = [2, 6, 11, 14, 19, 25, 30, 39, 43]
# B= 4
s = Solution()
print(s.solve(A, B))
