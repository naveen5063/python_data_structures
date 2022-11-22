class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        rem_hm = dict()
        for i in range(0, len(A)):
            A[i] %= 4
            if A[i] in rem_hm:
                rem_hm[A[i]] += 1
            else:
                rem_hm[A[i]] = 1

        print("hm", rem_hm)
        op = 0
        left = 0
        if 0 in rem_hm and len(rem_hm) < 1:
            return -1
        else:
            if 1 in rem_hm and 3 in rem_hm:
                op = min(rem_hm[1], rem_hm[3])
                left = max(rem_hm[1], rem_hm[3]) - min(rem_hm[1], rem_hm[3])
                if left % 2 == 1:
                    return -1
                op += left / 2
            else:
                if 1 in rem_hm:
                    if rem_hm[1] % 2 == 1:
                        return -1
                    rem = rem_hm[1] / 2
                    op += rem
                    op += rem / 2

                if 3 in rem_hm:
                    if rem_hm[3] % 2 == 1:
                        return -1
                    rem = rem_hm[3] / 2
                    op += rem
                    op += rem / 2


                # op = min(rem_hm[1], rem_hm[3])
                # left = max(rem_hm[1], rem_hm[3]) - min(rem_hm[1], rem_hm[3])
                # if left % 2 == 1:
                #     return -1
                # op += left / 2
            if 2 in rem_hm:
                if left > 0:
                    rem_hm[2] += left / 2
                if rem_hm[2] % 2 == 1:
                    return -1

                op += rem_hm[2] / 2
            return int(op)
        return 0


A = [1, 3, 4, 4, 2, 2]
A = [1, 3, 1, 3]
A = [2, 2, 2, 2]
A = [1, 1, 1, 1]
#A = [3, 3, 3, 3]
s = Solution()
print(s.solve(A))