class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack1 = []
        postfixexp = ""
        expdict = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ")": 3, '^': 3}
        for val in A:
            if val not in expdict.keys():
                postfixexp += val
            elif val == "(":
                stack1.append(val)
            elif val == ")":
                while stack1 and stack1[-1] != "(":
                    postfixexp += stack1.pop()
                stack1.pop()
            else:
                while stack1 and stack1[-1] != "(" and expdict[stack1[-1]] >= expdict[val]:
                    postfixexp += stack1.pop()
                stack1.append(val)
        while len(stack1) > 0:
            postfixexp += stack1.pop()

        print("ps", postfixexp)


A = "x^y/(a*z)+b"
# "xy^az*/b+"
A = "a+b*(c^d-e)^(f+g*h)-i"
# "abcd^e-fgh*+^*+i-"
# "abcd^e-fgh*+^*i-+"
# "abcd^e-^fgh*+*+i-
s = Solution()
s.solve(A)
