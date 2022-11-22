import sys
sys.setrecursionlimit(1000000)
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A, C):

        num = A

        # To take input from the user
        # num = int(input("Enter a number: "))

        factorial = 1

        # check if the number is negative, positive or zero
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1, num + 1):
                factorial = factorial * i
            print("The factorial of", num, "is", factorial)
        # if A == 1 or A == 0:
        #     return 1
        # else:
        #     return (self.solve(A-1, C) * A)%C


A = 4
A = 43211
C = 1191601
s = Solution()
print(s.solve(A, C))