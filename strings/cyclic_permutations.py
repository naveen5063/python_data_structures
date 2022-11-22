class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        lps_string = "{}${}{}".format(B, A, A)
        lps = [0]
        print("lps",lps)
        lps_count = 0
        for i in range(1, len(lps_string)):
            x = lps[i-1]
            while lps_string[x] != lps_string[i]:
                if x == 0:
                    x -= 1
                    break
                x = lps[x-1]
            lps.append(x + 1)
        print("lps", lps)
        for val in lps:
            if val == len(B):
                lps_count += 1
        # if lps_count > len(B):
        #     return lps_count -1
        return lps_count




A = "1001"
B = "0011"

# A = "ABCD"
# B = "ABCD"

# A = "111"
# B = "111"

A = "1101111111"
B = "1101111111"

s = Solution()
print(s.solve(A, B))