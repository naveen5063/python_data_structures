class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        maxindex = 0
        totalsumwithoutmaxval = A[0]
        for i in range(1, len(A)):
            totalsumwithoutmaxval += A[i]
            if A[i] > A[maxindex]:
                maxindex = i
        #print(totalsumwithoutmaxval)
        #totalsumwithoutmaxval -= A[maxindex]
        totalsum = A[maxindex] * len(A)
        print(totalsum)
        print(totalsumwithoutmaxval)
        return totalsum - totalsumwithoutmaxval


A = [2, 4, 1, 3, 2]
12
8

A = [ 731, 349, 490, 781, 271, 405, 811, 181, 102, 126, 866, 16, 622, 492, 194, 735 ]
s = Solution()
print(s.solve(A))
