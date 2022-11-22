class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        stack1 = []
        stack2 = []
        stack1.append(A[0])
        for i in range(1, len(A)):
            if A[i] > stack1[-1]:
                stack1.append(A[i])
            else:
                while len(stack1) != 0 and A[i] < stack1[-1]:
                    stack2.append(stack1[-1])
                    stack1.pop()
                stack1.append(A[i])
                while len(stack2) != 0:
                    stack1.append(stack2[-1])
                    stack2.pop()
        return stack1

A = [5, 17, 100, 11]
#[5, 11, 17, 100]
s = Solution()
print(s.solve(A))