class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        arr_len = len(A)
        pf_gcd = self.get_pf_gcd(A, arr_len)
        sf_gcd = self.get_sf_gcd(A, arr_len)
        ans = self.get_max_gcd(A, arr_len, pf_gcd, sf_gcd)
        return ans

    def get_max_gcd(self, A, arr_len, pf_gcd, sf_gcd):
        ans = 0
        for i in range(0, len(A)):
            # delete ith ele
            if i == 0:
                left = 0
                right = sf_gcd[i + 1]
            elif i == arr_len - 1:
                left = pf_gcd[i - 1]
                right = sf_gcd[i]
            else:
                left = pf_gcd[i - 1]
                right = sf_gcd[i + 1]
            ans = max(ans, self.gcd(left, right))
        return ans

    def get_sf_gcd(self, A, arr_len):
        sf_gcd = [0] * arr_len
        sf_gcd[arr_len - 1] = A[arr_len - 1]
        for j in range(arr_len - 2, -1, -1):
            sf_gcd[j] = self.gcd(A[j], sf_gcd[j + 1])
        return sf_gcd

    def get_pf_gcd(self, A, arr_len):
        pf_gcd = [0] * arr_len
        pf_gcd[0] = A[0]
        for i in range(1, arr_len):
            pf_gcd[i] = self.gcd(pf_gcd[i - 1], A[i])
        return pf_gcd

    def gcd(self, A, B):
        if B == 0: return A
        return self.gcd(B, A % B)


A = [12, 15, 18]
# 6
A = [5, 15, 30]
s = Solution()
print(s.solve(A))
