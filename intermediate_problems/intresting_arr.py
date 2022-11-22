class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        res = 0
        for i in range(0, len(A)):
            print("A[i", A[i])
            res = res ^ A[i]
        print("res", res)
        if res % 2 == 0:
            return "Yes"
        return "No"

# int
# result = 0;
# for (int i=0;i < A.size();i++){
# result = result ^ A.get(i);
# }
# if (result % 2 == 0)
#     return "Yes";
# else
#     return "No";

A = [9, 17, 22]
s = Solution()
print(s.solve(A))
