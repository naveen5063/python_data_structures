class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq_count = 0
        for i in range(len(A)-1, -1, -1):
            #print("i", i)
            if A[i] == "b" and A[i-1] == "o" and A[i-2] == "b":
                freq_count += 1
        print("Fre", freq_count)
        return freq_count


A = "bobabtbobl"
s = Solution()
s.solve(A)

# n=len(A)
# ans="bob"
# coun=0
# for i in range(n-2):
#     if A[i:i+3]==ans:
#         coun+=1
# return coun
