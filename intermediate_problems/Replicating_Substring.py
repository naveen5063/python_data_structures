class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):

        if A == 1:
            return 1

        freq_dict = {}
        total_count = 0
        for val in B:
            if val in freq_dict.keys():
                freq_dict[val] += 1
            else:
                freq_dict[val] = 1

        for item in freq_dict:
            if freq_dict[item] % A != 0:
                return -1
            total_count += freq_dict[item]

        if len(freq_dict) == 1 and total_count % A == 0:
            return 1

        if total_count % A == 0 and int(total_count / A) >= A:
            return 1

        return -1


A = 2
B = "bbaabb"
#
A = 1
B = "bc"

A = 2
B = "abab"
#
# A = 3
# B = "abcabcabc"
# #
# A = 5
# B = "aaaaa"
# #
# A = 2
# B = "aaab"
#
# A = 5
# B = "xxxvgmocfqnchmxtxxujwoxuwiwrgpofmnauzryghllraikzheidtgxrqtiwkydyldumusteegvgohfynnbgvbznujjhhohuucjo"
#
# A = 4
# B = "zngtrsewyuafbrqpzfiilcuzbhjcvlewynqqfumfoolrhbigjqqwslxuuiwrtdnsqdixawcqmpittsbcjrabexxyfwpzzdtpidmk"

s = Solution()
print("ans", s.solve(A, B))
