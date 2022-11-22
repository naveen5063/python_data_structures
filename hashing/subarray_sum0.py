class Solution:
    # @param A : list of integers
    # @return an integer
    # def solve(self, A):
    #     for i in range(0, len(A)):
    #         sum = 0
    #         for j in range(i, len(A)):
    #             sum += A[j]
    #             if sum == 0:
    #                 return 1
    #     return 0

    def solve(self, A):
        hash_set = set()
        hash_set.add(0)
        print("hashset", hash_set)
        sum = 0
        for i in range(0, len(A)):
            print("hs", hash_set)
            sum = A[i] + sum
            print("sum", sum)
            if sum in hash_set:
                return 1
            else:
                hash_set.add(sum)

            print("------------")
        return 0


A = [1, 2, 3, 4, 5]
# A = [-1, 1]
#A = [1, 2, -3]
#A = [96, -71, 18, 66, -39, -32, -16, -83, -11, -92, 55, 66, 93, 5, 50, -45, 66, -28, 69, -4, -34, -87, -32, 7, -53, 33,
#     -12, -94, -80, -71, 48, -93, 62]

#A = [-78, -97, -44, -18, -7, -26, 37, -76, -23, -35, 48, 9, 25, 62, -90, 27, -40, 18, 88, 82, 15, 96, 31, -2, -45, -48,
#     52, -78, -79, -76, -18, -88, -85, 58, -48, -48, -16, 77, -79, -89, -78, 27, 98, 53, -6, 43, 73, 38]

s = Solution()
print(s.solve(A))
