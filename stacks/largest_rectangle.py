class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):

        left_smallest = self.prevSmallerindex(A)
        right_smallest = self.nextSmallerindex(A)
        max_area = float('-inf')
        for i in range(len(A)):
            max_area = max(max_area, (right_smallest[i] - left_smallest[i] - 1) * A[i])
        return max_area

    def prevSmallerindex(self, A):
        stack = []
        arr = [-1 for i in range(0, len(A))]
        for i in range(0, len(A)):
            while len(stack) > 0 and A[i] <= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                arr[i] = stack[-1]
            stack.append(i)

        return arr

    def nextSmallerindex(self, A):
        stack = []
        arr = [-1 for i in range(0, len(A))]
        for i in range(len(A)-1, -1, -1):
            while len(stack) > 0 and A[i] <= A[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                arr[i] = stack[-1]
            stack.append(i)

        return arr

A = [2, 1, 5, 6, 2, 3]
#10
# A = [4, 7, -9, 5, -6, 9, 7, 5, 2, 10]
# A = [2, 9, 7, 1, 4, 7, 2, 6, 5]
s = Solution()
print(s.largestRectangleArea(A))