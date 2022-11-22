class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack1 = []
        expression = ["/", "+", "*", "-"]
        for val in A:
            if val in expression:
                exp = "{}{}".format(val, stack1.pop())
                exp = "{}{}".format(stack1.pop(), exp)
                res = eval(exp)
                stack1.append(int(res))
            else:
                stack1.append(val)
        return stack1[0]


A = ["2", "1", "+", "3", "*"]
# A = ["4", "13", "5", "/", "+"]
# 9
s = Solution()
print(s.evalRPN(A))
