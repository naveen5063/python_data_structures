class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return self.inver(A, 0, len(A) - 1) % (10 ** 9 + 7)

    def inver(self, A, start, end):
        if start == end:
            return 0
        print("s e", start, end)
        mid = (start + end) // 2
        print("mid", mid)
        l = self.inver(A, start, mid) % (10 ** 9 + 7)
        r = self.inver(A, mid + 1, end) % (10 ** 9 + 7)
        c = self.mergeinver(A, start, mid, end) % (10 ** 9 + 7)
        print("--", l, r, c)
        return (l + r + c) % (10 ** 9 + 7)

    def mergeinver(self, A, start, mid, end):
        merged_arr = [0] * (end - start + 1)
        p1 = start
        p2 = mid + 1
        p3 = 0
        count = 0
        while p1 <= mid and p2 <= end:
            if A[p1] <= A[p2]:
                merged_arr[p3] = A[p1]
                p1 += 1
                p3 += 1
            else:
                merged_arr[p3] = A[p2]
                p2 += 1
                p3 += 1
                count += (mid - p1) + 1

        while p1 <= mid:
            merged_arr[p3] = A[p1]
            p1 += 1
            p3 += 1

        while p2 <= end:
            merged_arr[p3] = A[p2]
            p2 += 1
            p3 += 1

        for i in range(0, end - start + 1):
            A[i + start] = merged_arr[i]
        # for i in range(start, end + 1):
        #     A[i] = merged_arr[i - start]
        return count % (10 ** 9 + 7)


A = [3, 2, 1]
A = [45, 10, 15, 25, 50]
s = Solution()
print(s.solve(A))
