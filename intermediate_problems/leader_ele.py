class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        c = 1
        leader_arr = []
        max_ele = A[len(A)-1]
        leader_arr.append(max_ele)
        for i in range(len(A)-2, 0, -1):
            if A[i] > max_ele:
                c += 1
                max_ele = A[i]
                leader_arr.append(max_ele)
        print(leader_arr)
        return c


A = [16, 17, 4, 3, 5, 2]
s = Solution()
print(s.solve(A))