class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min_val = min(A)
        max_val = max(A)
        min_index = -1
        max_index = -1
        min_len = len(A)
        if min_val == max_val:
            return 1
        for i in range(len(A) - 1, -1 , -1):
            if A[i] == min_val:
                min_index = i
                if max_index != -1:
                    arr_len = max_index - min_index
                    min_len = min(min_len, arr_len)
            elif A[i] == max_val:
                max_index = i
                if min_index != -1:
                    arr_len = min_index - max_index
                    min_len = min(min_len, arr_len)
            print("min_index", min_index)
            print("max_index", max_index)
        return min_len + 1



A = [1, 3]
A = [1, 3, 4 , 2, 5, 2, 1]
s = Solution()
print(s.solve(A))