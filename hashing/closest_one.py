import json
from collections import OrderedDict


class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A):
        od = OrderedDict()
        for i in range(0, len(A))
            type = A[i][0]
            index = A[i][1]
            if type == 1:
                if index in od:
                    od.pop(index)
                else:
                    od.


A = [[1, 5], [1, 15], [1, 8], [1, 1], [2, 10]]
s = Solution()
s.solve(A)