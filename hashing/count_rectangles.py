class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        points_map = set()
        rectangle_count = 0
        for i in range(0, len(A)):
            points = f'{A[i]}@{B[i]}'
            points_map.add(points)

        for i in range(0, len(A)):
            for j in range(i + 1, len(A)):
                x1, y1, x2, y2 = A[i], B[i], A[j], B[j]
                if y1 == y2 or x1 == x2:
                    continue
                p4 = f'{x1}@{y2}'
                p3 = f'{x2}@{y1}'
                if p3 in points_map and p4 in points_map:
                    rectangle_count += 1
        return int(rectangle_count/2)

A = [1, 1, 2, 2]
B = [1, 2, 1, 2]

A = [1, 1, 2, 2, 3, 3]
B = [1, 2, 1, 2, 1, 2]

s = Solution()
print(s.solve(A, B))
