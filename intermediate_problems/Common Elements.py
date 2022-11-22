class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, arr1, arr2):
        common_elements = []
        arr1_dict = {}
        for val in arr1:
            if val in arr1_dict:
                arr1_dict[val] += 1
            else:
                arr1_dict[val] = 1

        for val in arr2:
            if val in arr1_dict:
                common_elements.append(val)
                arr1_dict[val] -= 1
                if arr1_dict[val] == 0:
                    del arr1_dict[val]

        return common_elements

A = [1, 2, 2, 1]
B = [2, 3, 1, 2]

#[1, 2, 2]

A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]

#[2, 10]

s = Solution()
print(s.solve(A, B))