class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        pairs = []
        count = 1
        for i in range(len(A)):
            pairs.append([B[i], A[i]])
        pairs.sort()
        print(pairs)
        selected_pair = pairs[0]

        print(selected_pair)
        for j in range(1, len(pairs)):
            print("pairs[j][0]", pairs[j][1], selected_pair[0])
            if pairs[j][1] >= selected_pair[0]:
                selected_pair = pairs[j]
                count += 1
        print(count)



A = [1, 5, 7, 1]
B = [7, 8, 8, 8]

A = [3, 2, 6]
B = [9, 8, 9]
A = [ 3, 13, 7, 7, 10, 3 ]
B = [ 6, 15, 9, 8, 16, 11 ]
s = Solution()
s.solve(A, B)