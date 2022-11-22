from functools import cmp_to_key


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        normal = sorted(A)
        print("mormal", normal)
        print("A", A)
        A = list(map(str, A))

        def compare(num1, num2):
            print("--- ", num1, num2, "----",  num1 + num2, num2 + num1)
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        print("A", A)
        A = sorted(A, key=cmp_to_key(compare))
        if A[0] == '0':
            return 0
        print("A", A)
        return "".join(A)


A = [3, 30, 34, 5, 9]

# A = [2, 3, 9, 0]

s = Solution()
print(s.largestNumber(A))
