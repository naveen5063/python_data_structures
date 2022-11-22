class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        new_list = []
        while A:
            min = A[0]
            print("min", min)
            for x in A:
                if x < min:
                    print("x", x)
                    min = x
            print("new_listbf ", new_list)
            new_list.append(min)
            print("new_list", new_list)
            A.remove(min)
            print("A", A)
        return new_list

A = [0, 1, 2, 0, 1, 2]
s = Solution()
print(s.sortColors(A))