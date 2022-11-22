class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ans = -1
        equilibrium_index = []
        prefix_sum_arr = self.get_prefix_sum(A)
        for i in range(0, len(prefix_sum_arr)):
            if i == 0:
                left = 0
                right = prefix_sum_arr[len(prefix_sum_arr) - 1] - prefix_sum_arr[i]
            else:
                left = prefix_sum_arr[i - 1]
                right = prefix_sum_arr[len(prefix_sum_arr) - 1] - prefix_sum_arr[i]
            if left == right:
                equilibrium_index.append(i)
                ans = equilibrium_index[0]
        return ans

    def get_prefix_sum(self, A):
        pf_sum = []
        pf_sum.insert(0, A[0])
        for i in range(1, len(A)):
            index_sum = pf_sum[i - 1] + A[i]
            pf_sum.insert(i, index_sum)
        return pf_sum

#A=[-7, 1, 5, 2, -4, 3, 0]
A=[1,2,3]
s= Solution()
print(s.solve(A))