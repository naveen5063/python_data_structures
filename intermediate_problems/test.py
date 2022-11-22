class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Creating Even and Odd PF(Prefix sum)
        N = len(A)
        evenPF = [0 for x in range(N)]
        oddPF = [0 for x in range(N)]
        evenPF[0] = A[0]
        oddPF[0] = 0
        for i in range(1, N):
            if i % 2 == 0:
                evenPF[i] = evenPF[i - 1] + A[i]
                oddPF[i] = oddPF[i - 1]
            else:
                evenPF[i] = evenPF[i - 1]
                oddPF[i] = oddPF[i - 1] + A[i]

        # Finding count of indexes
        count = 0
        for i in range(N):
            if i == 0:
                even_Sum = oddPF[N - 1]
                odd_Sum = evenPF[N - 1] - evenPF[0]
            else:
                even_Sum = evenPF[i - 1] + oddPF[N - 1] - oddPF[i]
                odd_Sum = oddPF[i - 1] + evenPF[N - 1] - evenPF[i]

            if even_Sum == odd_Sum:
                count += 1

        return count

A = [2, 1, 6, 4]
A = [1, 1, 1]
s = Solution()
print("out ",s.solve(A))