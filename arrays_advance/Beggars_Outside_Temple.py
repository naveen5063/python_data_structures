class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        arr = [0]*A
        for i in range(0, len(B)):
            start = B[i][0]-1
            end = B[i][1]-1
            value = B[i][2]
            print(start, end, value)
            arr[start] += value
            if end+1 < A:
                arr[end+1] -= value

        print(arr)
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        print(arr)

A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
s = Solution()
s.solve(A, B)