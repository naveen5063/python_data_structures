class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A == 0:
            return 0
        elif A == 1 or A == 2:
            return 1
        else:
            return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)




A = 9
A = 0
s = Solution()
print(s.findAthFibonacci(A))