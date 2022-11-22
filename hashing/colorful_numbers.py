class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        unique_prod = set()
        numarr = str(A)
        for i in range(len(numarr)):
            product = 1
            for j in range(i, len(numarr)):
                product *= int(numarr[j])
                if product in unique_prod:
                    return 0
                unique_prod.add(product)
        return 1


A = 23
A = 236

s = Solution()
print(s.colorful(A))
