from collections import deque


class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        q1 = deque()
        q1.append(11)
        q1.append(22)
        cnt = 2
        start = 0
        end = 2
        if A <= 2:
            if A == 1:
                return 11
            if A == 2:
                return 22
        else:
            while cnt < A:
                numcnt = 0
                for i in range(0, 2):
                    strval = str(q1[i])
                    for j in range(start, end):
                        if cnt < A:
                            res_first, res_second = strval[:len(strval) // 2], strval[len(strval) // 2:]
                            num = "{}{}{}".format(res_first, q1[j], res_second)
                            q1.append(int(num))
                            numcnt += 1
                            cnt += 1
                start = end
                end += numcnt
            return num


A = 7
# 22
# A = 4
A = 14
A = 40
# 1211221121
# 1211221121
# 12122121
s = Solution()
print(s.solve(A))
