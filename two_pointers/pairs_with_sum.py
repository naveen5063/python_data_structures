class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        mod = 1000 * 1000 * 1000 + 7
        ans = 0
        i = 0
        j = len(A) - 1
        p1 = -1
        p2 = -1
        #count = 0
        print("A", A)

        while i < j:
            print("ij bf", i, j)
            sum = A[i] + A[j]
            print("ij", i, j)
            print("sum ", sum)
            if sum == B:
                count = 0
                prev = j
                while prev > i and A[j] == A[prev]:  # // count duplicate values from right pointer
                    count += 1
                    prev -= 1
                ans = (ans + count) % mod
                j += 1
            elif sum < B:
                i += 1
            else:
                j -= 1
        return count


A = [1, 1, 1]
B = 2

A = [1, 1]
B = 2

# A = [ 1, 2, 6, 6, 7, 9, 9 ]
# B = 13

# A = [ 2, 3, 3, 5, 7, 7, 8, 9, 9, 10, 10 ]
# B = 11

# A = [ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 9, 10 ]
# B = 5


s = Solution()
print(s.solve(A, B))
