def swap_elements(A, start_index, end_index):
    A[start_index], A[end_index] = A[end_index], A[start_index]
    return A

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        reversed_array = []
        print("len" , len(A))
        for i in range(len(A)-1, -1, -1):
            print(i)
            reversed_array.append(A[i])
        # start_index = 0
        # end_index = len(A) -1
        # while start_index <= end_index:
        #     print(start_index, end_index)
        #     A = swap_elements(A, start_index, end_index)
        #     start_index += 1
        #     end_index -= 1
        return reversed_array

s= Solution()
A = [1,2,3,2,1]
print(s.solve(A))