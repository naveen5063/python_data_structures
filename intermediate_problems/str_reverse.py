class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        val = A.strip()
        val = val.split(" ")
        start = 0
        end = len(val) - 1
        while start <= end:
            val[start], val[end] = val[end].strip(), val[start].strip()
            start += 1
            end -= 1
        return ' '.join(val)


#single string
A = "scaler"
# relacs

#muliple string
A = "the sky is blue"
# "blue is sky the"
A = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "
#hv xdq op qoddptokkz vemmoxrgf ombt gg crulgzfkif
A = "anish is name my"
s = Solution()
print(s.solve(A))