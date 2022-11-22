# class Solution {
# int catalan_Number(int n)
# {
# int catalan[n+1];
# catalan[0] = catalan[1] = 1;
#
# for (int i=2;i <= n;++i)
# {
# catalan[i] = 0;
# for (int j=0;j < i;++j)
# catalan[i] += catalan[j] * catalan[i-j-1];
# }
#
#
# return catalan[n];
# }
# public:
# int
# numTrees(int
# n) {
# return catalan_Number(n);
# }
# };


class unique_BST():

    def catalan(self, n):
        if n == 0 or n == 1:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(n + 1)]
        print("catalan", catalan)

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, n + 1):
            print("i", i)
            catalan[i] = 0
            for j in range(1, i+1):
                print("j", j , j - 1, i - j)
                print("values",j - 1, i - j+1)
                catalan[i] += catalan[j-1] * catalan[i - j]
                print("catalan[i]", catalan[i])
            print("catalin", i , catalan[i])

        # Return last entry
        return catalan[n]


u = unique_BST()
print(u.catalan(3))