class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        p1 = 0
        p2 = 1
        count = 0
        while p1 < len(A) and p2 < len(A):
            if A[p1] + A[p2] == B:
                print(A[p1], A[p2], B)
                count += 1
                p2 += 1
                #print("count", count)
            elif A[p1] + A[p2] < B:
                p1 += 1
            else:
                p2 += 1
        return count


A = [1, 1, 1]
B = 2

# A = [1, 1]
# B = 2

# A = [ 2, 3, 5, 6, 10 ]
# B = 6
s = Solution()
print(s.solve(A, B))
