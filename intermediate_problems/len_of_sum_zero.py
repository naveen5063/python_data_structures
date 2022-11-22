class Solution:
    def lszero(self, arr):
        ans = []
        dictionary = {}
        sumofele = 0
        prefix = []

        # Generate prefix array
        for i in range(len(A)):
            sumofele += A[i]
            prefix.append(sumofele)
        print("prefix", prefix)

        # Loop through the array and check if you find same eles(using dictionary) or 0:
        # if you do, update the ans if the length of the new ans is more
        for i in range(len(prefix)):
            print("prefix[i]", prefix[i])
            if prefix[i] == 0:
                if i + 1 > len(ans):
                    ans = A[:i + 1]
                    print("ans if 0", ans)
            if prefix[i] in dictionary:
                print("i", i)
                print("dictionary----", dictionary)
                print("dictionary[prefix[i]]----", dictionary[prefix[i]])
                print("i - dictionary[prefix[i]]----", i - dictionary[prefix[i]])
                print("len(ans)", len(ans))
                if i - dictionary[prefix[i]] > len(ans):
                    print("cmp", i - dictionary[prefix[i]],  len(ans))
                    print("rabge", dictionary[prefix[i]] + 1, i + 1)
                    ans = A[dictionary[prefix[i]] + 1: i + 1]
                    print("ans", ans)
            else:
                dictionary[prefix[i]] = i

        return ans

A = [0,2,-2,4,-4]
s = Solution()
print(s.lszero(A))