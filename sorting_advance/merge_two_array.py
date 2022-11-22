class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        combined_arr = [0]*(len(A)+len(B))
        p1 = 0
        p2 = 0
        p3 = 0
        while p1 < len(A) and p2 < len(B):
            if A[p1] < B[p2]:
                combined_arr[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                combined_arr[p3] = B[p2]
                p2 += 1
                p3 += 1

        while p1 < len(A):
            combined_arr[p3] = A[p1]
            p1 += 1
            p3 += 1
        while p2 < len(B):
            combined_arr[p3] = B[p2]
            p2 += 1
            p3 += 1

        return combined_arr

A = [4, 7, 9]
B = [2, 11, 19]
A = [1]
B = [2]
s = Solution()
print(s.solve(A, B))