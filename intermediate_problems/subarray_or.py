def cnt(n):
    return (n * (n + 1)) // 2

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # sum = 0
        # s1 = 0
        # mod = pow(10, 9) + 7
        # for i in range(0, len(A)):
        #     for j in range(i, len(A)):
        #         val = 0
        #         for k in range(i, j+1):
        #             val = val | A[k]
        #         sum += val
        #         #print("val", val)
        #         print("sum", sum)
        #         #s1 = sum % pow(10, 9)
        #         #print("s1", s1)
        # #print(sum)
        # s1 =  sum % (pow(10, 9) + 7)
        # print("s1", s1)
        # return sum


        MOD = int(1e9 + 7)
        print("MOD", MOD)
        ans = 0
        n = len(A)
        for b in range(27):
            c = 0
            print("n", n)
            C = cnt(n)
            print("out C", C)
            for i in range(n):
                print("A[i]", A[i])
                if A[i] & 1:
                    print(A[i] & 1)
                    C -= cnt(c)
                    print("C", C)
                    c = 0
                else:
                    c += 1
                A[i] >>= 1
                print("Ai out", A[i])
            C -= cnt(c)
            ans = (ans + (1 << b) * C) % MOD
        return ans

# secondly , efficient approach is
#
# you have to add contribution of each bit of each number
#
# contribution of a jth set bit of ith number is i*(1<<j)
#
# and contribution of a jth unset bit of ith number is (index of latest number with jth set bit)*(1<<j)
#
# so save all the set bits of a number and use them
#
# sending you code at slack

A = [1, 2, 3, 4, 5]
#A = [7, 8, 9, 10]
#A = [ 347148, 221001, 394957, 729925, 276769, 40726, 552988, 29952, 184491, 146773, 418965, 307, 219145, 183037, 178111, 81123, 109199, 683929, 422034, 346291, 11434, 7327, 340473, 316152, 364005, 359269, 170935, 105784, 224044, 22563, 48561, 165781, 9329, 357681, 169473, 175031, 605611, 374501, 6607, 329965, 76068, 836137, 103041, 486817, 195549, 107317, 34399, 56907, 37477, 189690, 36796, 376663, 39721, 177563, 174179, 183646, 217729, 408031, 429122, 631665, 282941, 526797, 262186, 306571, 63613, 57501, 70685, 226381, 1338, 9360, 130360, 20300, 400906, 87823, 180349, 108813, 18181, 119185, 1, 102611, 63591, 12889, 311185, 383896, 8701, 76077, 75481, 386017, 153553, 304913, 383455, 105948, 142885, 1, 12610, 137005, 119185, 16948, 66171, 123683 ]
s = Solution()
print(s.solve(A))