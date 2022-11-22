# import sys
# sys.setrecursionlimit(100000)

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        start = 0
        end = len(A) - 1
        self.merge_sort(A, start, end)
        return A

    def merge_sort(self, A, start, end):
        print("start", start)
        print("end", end)
        if start == end:
            return
        mid = (start + end) // 2
        self.merge_sort(A, start, mid)
        self.merge_sort(A, mid + 1, end)
        self.merge(A, start, mid, end)

    def merge(self, A, start, mid, end):
        merged_arr = [0]*(end - start + 1)
        p1 = start
        p2 = mid + 1
        p3 = 0
        while p1 <= mid and p2 <= end:
            if A[p1] <= A[p2]:
                merged_arr[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                merged_arr[p3] = A[p2]
                p2 += 1
                p3 += 1

        while p1 <= mid:
            merged_arr[p3] = A[p1]
            p1 += 1
            p3 += 1

        while p2 <= end:
            merged_arr[p3] = A[p2]
            p2 += 1
            p3 += 1

        for i in range(0, end - start + 1):
            A[i+start] = merged_arr[i]
A = [1, 4, 10, 2, 1, 5]
A = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
A = [1, 4, 10, 2, 1, 5]
#A = [3, 7, 1]
s = Solution()
print(s.solve(A))
#print(s.merge(A, 0, 1, 5))
