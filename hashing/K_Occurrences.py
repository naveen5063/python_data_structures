class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def getSum(self, A, B, C):
        freq_map = {}
        for i in range(A):
            if C[i] in freq_map:
                freq_map[C[i]] += 1
            else:
                freq_map[C[i]] = 1

        totol_weight = 0
        weight_added = 0
        for j in freq_map:
            if freq_map[j] == B:
                weight_added = 1
                totol_weight += j

        if not weight_added:
            return -1
        return totol_weight % 10000000007


A = 5
B = 2
C = [1, 2, 2, 3, 3]

A = 3
B = 2
C = [0, 0, 1]
s = Solution()
print(s.getSum(A, B, C))
