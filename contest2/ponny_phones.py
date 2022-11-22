class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers

    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid

        if x < arr[mid]:
            return mid - 1
        return mid

    def solve(self, A, B):
        for i in range(1, len(A)):
            A[i] = A[i - 1] + A[i]

        for i in range(0, len(B)):
            index = self.binary_search(A, B[i])
            B[i] = index + 1
        return B

A = [3, 4, 4, 6]
B = [20, 4, 10, 2]
s = Solution()
print(s.solve(A, B))