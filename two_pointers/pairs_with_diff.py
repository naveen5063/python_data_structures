class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        #A = list(set(A))
        A.sort()
        i = 0
        j = 1
        p1 = -1
        p2 = -1
        count = 0
        print("A", A)
        while j < len(A):
            diff = abs(A[j] - A[i])
            if diff == B:
                if p1 != A[j] and p2 != A[i]:
                    count += 1
                    p1 = A[j]
                    p2 = A[i]
                i += 1
                j += 1
            elif diff > B:
                i += 1
                if i == j:
                    j += 1
            else:
                j += 1
        return count


A = [1, 5, 3, 4, 2]
B = 3

# A = [8, 12, 16, 4, 0, 20]
# B = 4
#
# A = [1, 1, 1, 2, 2]
# B = 0
#
# A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
# B = 0

s = Solution()
print(s.solve(A, B))
