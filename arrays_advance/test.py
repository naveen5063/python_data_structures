class Solution:

    def solvewithbf(self, A, k):
        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                if abs(A[j] - A[i]) == k:
                    return "YES"
        return "NO"

    def solvewithhashing(self, A, k):
        hashset = set()
        for val in A:
            if val not in hashset:
                hashset.add(val)

        for val in A:
            if val + k in hashset or val - k in hashset:
                return "YES"
        return "NO"
        # print(hashset)

    def solvewithsorting(self, arr, k):
        arr.sort()
        p1 = 0
        p2 = 1
        while p2 < len(arr):
            if A[p2] - A[p1] == k or A[p1] - A[p2] == k:
                return "YES"
            elif A[p2] - A[p1] > k:
                p1 += 1
                if p1 == p2:
                    p2 += 1
            else:
                p2 += 1
        return "NO"


A = [1, 5, 3, 8]

A = [1, 3, 5, 8]

k = 7
# A = [1]
#
# A = [1, 2, 1]
# k = 0

# A = [3, 4, 2, 1, 6]
# k = 3
s = Solution()
# print(s.solvewithbf(A, k))
# print(s.solvewithhashing(A, k))
print(s.solvewithsorting(A, k))
