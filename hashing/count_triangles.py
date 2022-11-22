class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        x_axis_freq = {}
        y_axis_freq = {}
        for x_axis in A:
            if x_axis in x_axis_freq:
                x_axis_freq[x_axis] += 1
            else:
                x_axis_freq[x_axis] = 1

        for y_axis in B:
            if y_axis in y_axis_freq:
                y_axis_freq[y_axis] += 1
            else:
                y_axis_freq[y_axis] = 1

        triangle_count = 0
        for i in range(0, len(A)):
            x_axis_count = x_axis_freq[A[i]]
            y_axis_count = y_axis_freq[B[i]]
            triangle_count += (x_axis_count - 1) * (y_axis_count - 1)
        return triangle_count


A = [1, 1, 2]
B = [1, 2, 1]

A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]

s = Solution()
print(s.solve(A, B))
