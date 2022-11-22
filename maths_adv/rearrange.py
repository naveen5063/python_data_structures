class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        arr_len = len(A)
        for i in range(0, arr_len):
            A[i] *= len(A)

        for i in range(0, arr_len):
            ind = int(A[i]/arr_len)
            val = int(A[ind]/arr_len)
            A[i] += val

        for i in range(0, arr_len):
            A[i] %= arr_len

        return A


# Input: [1, 0]
# Return: [0, 1]

A = [3, 1, 4, 6, 5, 0, 2]
s = Solution()
print(s.arrange(A))