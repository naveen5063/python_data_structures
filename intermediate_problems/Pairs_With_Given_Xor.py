class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hashset = set()
        res = 0
        for elem in A:
            temp = B ^ elem
            print(temp, B, elem)
            if temp in hashset:
                print("temp", temp)
                res += 1
            else:
                hashset.add(elem)

        return res


A = [5, 4, 10, 15, 7, 6]
B = 5

A = [3, 6, 8, 10, 15, 50]
B = 5

s = Solution()
print(s.solve(A, B))
