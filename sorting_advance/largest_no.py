import functools
class Solution:
  # @param A : tuple of integers
    # @return a strings


    def compare(self, a, b):
        print("A", a, b)
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return -1  # no need to swap
        elif int(str(a) + str(b)) < int(str(b) + str(a)):
            return 1  # Swap
        else:
            return 0  # do nothing

    def largestNumber(self, A):
        l = []
        for i in sorted(A, key=functools.cmp_to_key(self.compare)):
            l.append(str(i))

        o = str(int("".join(l)))
        print("o", o)
        #return str(int("".join([str(i) for i in sorted(A, key=functools.cmp_to_key(self.compare))])))

A = [3, 30, 34, 5, 9]
# [9, 5, 34, 3, 30]
# "9534330"
A = [ 0, 0, 0, 0, 0 ]
#A = [2, 3, 9, 0]
s = Solution()
print(s.largestNumber(A))