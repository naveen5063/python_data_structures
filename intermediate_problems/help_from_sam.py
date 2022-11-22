class Solution:
    # @param A : integer
    # @return an integer

    # def power_of_two(self, x):
    #     return (x and (not(x & (x - 1))) )
    #
    # def solve(self, A):
    #     if A != 0:
    #         if self.power_of_two(A):
    #             return 1
    #         else:
    #             return 2
    #     else:
    #         return 0
    def solve(self, A):
        count = 0
        while(A > 0):
            if ((A & 1) == 1):
                count +=1
            A = A >> 1
        return count


# Input 1: A = 5
#
# Output1:2
# Initialscore: 0
# Takes help from Sam, score: 1
# Alex solves a question, score: 2
# Alex solves a question, score: 4
# Takes help from Sam, score: 5

A = 7
s = Solution()
print(s.solve(A))