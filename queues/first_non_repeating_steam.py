from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = deque()
        freq_arr = [0] * 26
        ans = ""
        for val in A:
            freq_arr[ord(val) - ord('a')] += 1

            if freq_arr[ord(val) - ord('a')] == 1:
                q.append(val)

            while len(q) > 0 and freq_arr[ord(q[0]) - ord('a')] > 1:
                q.remove(q[0])

            if len(q) > 0:
                ans += q[0]
            else:
                ans += "#"

        return ans


A = "abadbc"
#A = "ababc"
A = "gu"
A = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
s = Solution()
print(s.solve(A))





