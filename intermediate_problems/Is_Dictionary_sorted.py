class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        aph = {}
        for i in range(len(B)):
            aph[B[i]] = i

        def helper(S1, S2):
            N = min(S1, S2)
            bool = False
            for i in range(len(N)):
                s1val = aph.get(S1[i])
                s2val = aph.get(S2[i])
                print("s", S1[i], S2[i], s1val, s2val)
                if s1val < s2val:
                    bool = True
                    break
                if s1val > s2val:
                    bool = False
                    break
            return bool

        prev = 0
        for j in range(1, N):
            if prev > aph.get(A[j][0]):
                return 0

            if aph.get(A[j][0]) == prev:
                v1 = A[j - 1]
                v2 = A[j]
                print(v1, v2)
                res = helper(v1, v2)
                if res:
                    pass
                else:
                    return 0
            prev = aph.get(A[j][0])

        return 1


A = ["hello", "scaler", "interviewbit"]
B = "adhbcfegskjlponmirqtxwuvzy"

A = ["fine", "none", "no"]
B = "qwertyuiopasdfghjklzxcvbnm"

s = Solution()
print(s.solve(A, B))
