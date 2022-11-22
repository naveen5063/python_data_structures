class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hmap = dict()
        minDistance = 10 ** 9
        print(minDistance)
        # Initialize previousIndex
        # and currentIndex as 0
        previousIndex = 0
        currentIndex = 0

        # Traverse the array and
        # find the minimum distance
        # between the same elements with map
        for i in range(len(A)):
            print("hmap", hmap)
            print("A[i]", A[i])
            if A[i] in hmap:
                currentIndex = i

                # Fetch the previous index from map.
                previousIndex = hmap[A[i]]
                print("currentIndex", currentIndex)
                print("previousIndex", previousIndex)
                # Find the minimum distance.
                minDistance = min((currentIndex -
                                   previousIndex), minDistance)

            # Update the map.
            hmap[A[i]] = i

        # return minimum distance,
        # if no such elements found, return -1
        if minDistance == 10 ** 9:
            return -1
        return minDistance

A = [7, 1, 3, 4, 1, 7]
s = Solution()
print(s.solve(A))