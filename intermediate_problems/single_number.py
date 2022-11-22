class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        # def Diff(li1, li2):
        #     li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        #     return li_dif
        #
        # double_ele_list = []
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         if A[i] == A[j]:
        #             double_ele_list.append(A[i])
        #     if A[i] not in double_ele_list:
        #         return A[i]

        # for i in A:
        #     print(i)
        #     if i not in double_ele_list:
        #         print("res", A[i])
        # diff = Diff(A, double_ele_list)
        # print(diff[0])
        ans = 0
        for i in range(len(A)):
            ans = ans ^ A[i]
            print("i", A[i])
            print("ans", ans)
        return ans



A = [1, 2, 2, 3, 1]
s = Solution()
print(s.singleNumber(A))