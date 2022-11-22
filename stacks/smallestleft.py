
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        arr = [-1 for i in range(0, len(A))]
        for i in range(0, len(A)):
            while len(stack) > 0 and A[i] <= stack[-1]:
                stack.pop()
            if len(stack) > 0:
                arr[i] = stack[-1]
            stack.append(A[i])

        return arr

A = [4, 5, 2, 10, 8]
#[-1, 4, -1, 2, 2]
s = Solution()
print(s.prevSmaller(A))