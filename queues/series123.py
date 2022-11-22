from collections import deque



class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        if A >= 3:
            q = deque()
            q.append(1)
            q.append(2)
            q.append(3)
            cnt = 3
            p1 = 0
            while cnt != A:
                val = q[p1]
                if cnt < A:
                    q.append(val * 10 + 1)
                    cnt += 1
                if cnt < A:
                    q.append(val * 10 + 2)
                    cnt += 1
                if cnt < A:
                    q.append(val * 10 + 3)
                    cnt += 1
                p1 += 1
            return q
        else:
            q = deque()
            for i in range(1, A+1):
                q.append(i)
            return q

A = 7
A = 2
s = Solution()
print(s.solve(A))