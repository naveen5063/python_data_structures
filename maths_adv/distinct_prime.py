import math


def isprime(num):
    c = 0
    num_val = int(math.sqrt(num))
    for i in range(1, num_val + 1):
        if num % i == 0:
            if i == int(num / i):
                c += 1
            else:
                c += 2
    if c == 2:
        return True
    else:
        return False

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        distinct_prime_count = 0
        spf_arr = list(range(0, A + 1))
        for i in range(2, math.ceil(math.sqrt(A)) + 1):
            if i == spf_arr[i]:
                for j in range(i * i, A + 1, i):
                    if spf_arr[j] == j:
                        spf_arr[j] = i

        for i in range(1, A+1):
            c = 0
            list_prime = []
            x = i
            while x >= 2:
                if isprime(spf_arr[x]):
                    list_prime.append(spf_arr[x])
                    x = int(x / spf_arr[x])
                    c += 1
            if list_prime:
                distinct_vals = set(list_prime)
                if len(distinct_vals) == 2:
                    distinct_prime_count += 1

        return distinct_prime_count

#A = 4
# 1
#A = 12
A = 10
# 3
s = Solution()
print(s.solve(A))