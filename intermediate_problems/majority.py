class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        sorted_array = sorted(A)
        ele = sorted_array[0]
        freq = 1
        for i in range(1, len(sorted_array)):
            if freq == 0:
                ele = sorted_array[i]
                freq += 1
            elif ele != sorted_array[i]:
                freq -= 1
            else:
                freq += 1
        return ele




A = [2, 1, 2]
s = Solution()
print(s.majorityElement(A))
