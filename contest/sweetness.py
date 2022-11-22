import math


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer

    @staticmethod
    def is_prime(A):
        c = 0
        for i in range(1, int(math.sqrt(A)) + 1):
            if A % i == 0:
                if i == A:
                    c += 1
                c += 2
        if c == 2:
            return True
        return False

    @staticmethod
    def get_prime_hs(A):
        prime_set = set()
        for i in range(0, len(A)):
            # print("val", A[i])
            if Solution.is_prime(A[i]):
                prime_set.add(A[i])
        return prime_set

    @staticmethod
    def check_bit(i, j):
        if (i >> j) & 1 == 1:
            return True
        return False

    def solve(self, A, B, C):
        primeset = Solution.get_prime_hs(A)
        # print("ps", primeset)
        if primeset is None:
            return 0
        res = 0
        for i in range(1, int(math.pow(2, len(A)))):
            sum = 0
            c = 0
            for j in range(0, len(A)):
                if Solution.check_bit(i, j):
                    sum += A[j]
                    # print("A[j]", A[j])
                    if A[j] in primeset:
                        c += 1
            if c > 0 and B <= sum <= C:
                res += 1
        return res


A = [5, 43, 13, 51, 97, 29]
B = 9
C = 136
s = Solution()
print(s.solve(A, B, C))