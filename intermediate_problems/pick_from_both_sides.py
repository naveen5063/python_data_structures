class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_sum = A[0]
        back_sum, front_sum = self.front_back_sum(A, B)
        if front_sum > max_sum:
            max_sum = front_sum
        elif back_sum > max_sum:
            max_sum = back_sum
        print(front_sum)
        print(back_sum)
        print(max_sum)

    def front_back_sum(self, A, B):
        front_sum = 0
        back_sum = 0
        for i in range(0, B):
            print("A[i]", A[i])
            front_sum += A[i]
        stop_iter = len(A) - B
        for j in range(len(A) - 1, stop_iter - 1, -1):
            print("A[j]", A[j])
            back_sum += A[j]
        return back_sum, front_sum


A = [5, -2, 3, 1, 2]
B = 3
s=Solution()
s.solve(A, B)