class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        arr_dict = {}
        for val in arr:
            if val in arr_dict:
                arr_dict[val] += 1
            else:
                arr_dict[val] = 1

        for val in arr:
            if arr_dict[val] > 1:
                return val
        return -1



A = [10, 5, 3, 4, 3, 5, 6]
#A = [6, 10, 5, 4, 9, 120]

#5

#-1

s = Solution()
print(s.solve(A))