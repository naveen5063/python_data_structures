import math
from math import ceil, sqrt


class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, n):
        # val = -1
        # count = 0
        # while val != 0 and A > 0:
        # 	val = int(math.sqrt(A))
        # 	print(val)
        # 	val = A - pow(val, 2)
        # 	print(val)
        # 	A = val
        # 	count += 1
        # return count

        # Create a dynamic programming table
        # to store sq and getMinSquares table
        # for base case entries
        dp = [0, 1, 2, 3]

        # getMinSquares rest of the table
        # using recursive formula
        for i in range(4, n + 1):

            # max value is i as i can always
            # be represented as 1 * 1 + 1 * 1 + ...
            dp.append(i)

            # Go through all smaller numbers
            # to recursively find minimum
            for x in range(1, int(ceil(sqrt(i))) + 1):
                temp = x * x
                if temp > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i - temp])

        # Store result
        return dp[n]


A = 12
s = Solution()
print(s.countMinSquares(A))
