class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, key):
        res_arr = [-1, -1]
        ele_index = self.get_ele_index(A, key)
        print("ele_index", ele_index)
        for i in range(ele_index, len(A)):
            if A[i] == key:
                res_arr[1] = i
        for i in range(ele_index, -1, -1):
            if A[i] == key:
                res_arr[0] = i
        print("res", res_arr)

    def get_ele_index(self, A, key):
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if A[mid] == key:
                return mid
            elif A[mid] < key:
                low = mid + 1
            elif A[mid] > key:
                high = mid - 1
        return -1


A = [5, 7, 7, 8, 8, 8, 8, 10]
B = 8
A = [ 1 ]
B = 1
s = Solution()
s.searchRange(A, B)
