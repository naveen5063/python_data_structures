import sys


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        start_index = 0
        hm = {}
        maxlen = 1 - sys.maxsize
        index = sys.maxsize
        for i in range(0, len(A)):
            if A[i] < 0 and i < len(A):
                start_index = i + 1
            else:
                if start_index not in hm.keys():
                    hm[start_index] = [A[i]]
                else:
                    hm[start_index].append(A[i])
        print(hm)
        #index
        for val in hm:
            if len(hm[val]) == maxlen:
                index = min(index, val)
            if len(hm[val]) > maxlen:
                index = val
            maxlen = max(len(hm[val]), maxlen)
        return hm[index]


A = [5, 6, -1, 7, 8]
A = [1, 2, 3, 4, 5, 6]
A = [ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ]
# A = [ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ]
#A = [ -4549634, -3196682, 8455838, -1432628, -263819, -3928366, -5556259, -2114783, 3923939, -4183708 ]
# A = [ -3674875, 5305422, 7665178, 205505, -7168198, -1398091, 5392310, -1700856, 1259052, -3056006 ]

s = Solution()
print(s.solve(A))
