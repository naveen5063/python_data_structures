class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def getCombinationsUtil(self, a, sum, currIndex, result, curr):
        if sum == 0:
            #curr.sort()
            #print("curr", curr)
            #if curr not in result:
            result.append(list(curr))
            return
        elif sum < 0 or currIndex == len(a):
            return
        else:
            curr.append(a[currIndex])
            #print("curr", curr)
            self.getCombinationsUtil(a, sum - a[currIndex], currIndex + 1, result, curr)
            curr.pop()
            self.getCombinationsUtil(a, sum, currIndex + 1, result, curr)

    def getCombinations(self, a, sum):
        result = []
        curr = []
        index = 0
        a.sort()
        self.getCombinationsUtil(a, sum, index, result, curr)
        #print("result", result)
        unique_data = [list(x) for x in set(tuple(x) for x in result)]
        unique_data.sort()
        return unique_data
        #result.sort()
        #return result


A = [2, 3, 6, 7]
B = 7
A = [ 8, 10, 6, 11, 1, 16, 8 ]
B = 28

A = [2, 1, 3]
B = 3
s = Solution()
print("--", s.getCombinations(A, B))
