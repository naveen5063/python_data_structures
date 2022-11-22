class Solution:
    # @param A : string
    # @return an integer
   def solve(self, A):
         # maximum_consecutive_one = 0
         # start = 0
         # k = 1
         # zero_count = 0
         # for end in range(len(A)):
         #    print("A[end]", A[end])
         #    if A[end] == "0":
         #       zero_count += 1
         #       print("zero_count in end ", zero_count)
         #    while zero_count > k:
         #       print("A[start]", A[start])
         #       if A[start] == "0":
         #          zero_count -= 1
         #       start += 1
         #    print("end", end)
         #    print("zero_count", zero_count)
         #    print("start", start)
         #    maximum_consecutive_one = max(maximum_consecutive_one, end-start+1)
         #    print("max", maximum_consecutive_one)
         l = 0
         cnt = 0
         ans = 0
         for r in range(len(s)):
            print("s[r]", s[r])
            cnt += s[r] == "0"
            print(cnt)
            if cnt > 1:
               print("cnt", cnt)
               cnt -= s[l] == "0"
               l += 1
            print("r  l", r, l)
            ans = max(ans, r - l + 1)
            print("ans", ans)
         return min(ans, s.count("1"))

ob = Solution()
s = "111011101"
#s = "111000"
s = "010100110101"
#ob.solve(s)
print(ob.solve(s))