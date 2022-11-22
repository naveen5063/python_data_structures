import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_ele = max(A)
        final_prime = []
        prime_list = [True] * (max_ele + 1)
        prime_list[0], prime_list[1] = False, False
        for i in range(2, int(math.sqrt(max_ele))):
            if prime_list[i]:
                for j in range(i * i, max_ele, i):
                    prime_list[j] = True

        print(prime_list)
        for k in range(2, len(prime_list)):
            print("k", k)
            if prime_list[k]:
                final_prime.append(A[k - 1])

        return pow(2, len(final_prime)) - 1


# Input:
A = [1, 2, 3]
#
# Output:
# 3
s = Solution()
s.solve(A)
