class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        balanced_stack = []
        open_parenthesis = ["{", "(", "["]
        for parenthesis in range(len(A)):
            print("parenthesis", A[parenthesis])
            if A[parenthesis] in open_parenthesis:
                balanced_stack.append(A[parenthesis])
            elif (balanced_stack and
                  ((A[parenthesis] == "}" and balanced_stack[-1] == "{") or
                   (A[parenthesis] == ")" and balanced_stack[-1] == "(") or
                   (A[parenthesis] == "]" and balanced_stack[-1] == "["))):
                balanced_stack.pop()
            else:
                return 0
            print("balanced_stack", balanced_stack)
        print("balanced_stack out", balanced_stack)
        if balanced_stack:
            return 0
        return 1


A = "{([])}"
A = "(){"
# A = "()[]"
A = "({)}"
A = "))))))))"

s = Solution()
print(s.solve(A))
