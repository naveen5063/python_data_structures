class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ans = ""
        res = A + A
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(0, len(res)):
            if 96 < ord(res[i]) < 123:
                if res[i] in vowels:
                    ans += "#"
                else:
                    ans += res[i]
        return ans




A = "AbcaZeoB"
# "bc###bc###"
s = Solution()
print(s.solve(A))