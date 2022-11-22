import math

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans_arr = []
        n_val = max(A)
        final_arr = []
        spf_arr = list(range(0, n_val + 1))
        for i in range(2, math.ceil(math.sqrt(n_val)) + 1):
            if i == spf_arr[i]:
                for j in range(i * i, n_val + 1, i):
                    if spf_arr[j] == j:
                        spf_arr[j] = i

        for i in A:
            list_prime = []
            x = i
            while x > 1:
                list_prime.append(spf_arr[x])
                x = int(x / spf_arr[x])
            if list_prime:
                val = self.primefact(list_prime)
                ans_arr.append(val)
            else:
                ans_arr.append(1)
        return ans_arr

    def primefact(self, list_prime):
        ans = 1
        c = 0
        p = list_prime[0]
        for i in range(0, len(list_prime)):
            if p == list_prime[i]:
                c += 1
            else:
                ans = ans * (c + 1)
                c = 1
                p = list_prime[i]
        ans = ans * (c + 1)
        return ans

A = [2, 3, 4, 5]
#A = [8, 9, 10]
#A = [ 10, 20 ]
#A = [ 20, 39, 29, 51, 96, 32, 35, 50, 57, 7, 59, 51, 85, 55, 8, 26, 15, 4, 4, 18, 32, 49, 40, 46, 83, 77, 100, 92 ]
#arr [6, 4, 2, 4, 12, 6, 4, 6, 4, 2, 2, 4, 4, 4, 4, 4, 4, 3, 3, 6, 6, 3, 8, 4, 2, 4, 9, 6]

#"6 4 2 4 12 6 4 6 4 2 2 4 4 4 4 4 4 3 3 6 6 3 8 4 2 4 9 6 "

#A = [ 3, 52, 66, 64, 14, 51, 6, 39, 5, 26, 80, 88, 60, 73, 67, 16, 1, 81, 62, 42, 83, 31, 40, 4, 32, 31, 44, 3, 20, 94, 93, 57, 2, 18, 32, 59, 91, 30, 45 ]
#arr [2, 6, 8, 7, 4, 4, 4, 4, 2, 4, 10, 8, 12, 2, 2, 5, 1, 5, 4, 8, 2, 2, 8, 3, 6, 2, 6, 2, 6, 4, 4, 4, 2, 6, 6, 2, 4, 8, 6]
#A = [1, 2, 3]
#2 6 8 7 4 4 4 4 2 4 10 8 12 2 2 5 1 5 4 8 2 2 8 3 6 2 6 2 6 4 4 4 2 6 6 2 4 8 6
s = Solution()
print(s.solve(A))
