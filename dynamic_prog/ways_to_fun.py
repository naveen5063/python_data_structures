# long m = 1000000007;
# int x= 2;
# if(A>2) {
# x=A;
# }
# long dp[][] = new long[x + 1][3];
# dp[1][0] = 1;
# dp[1][1] = 1;
# dp[1][2] = 1;
# dp[2][0] = 3;
# dp[2][1] = 2;
# dp[2][2] = 2;
# for(int i=2; i<=A; i++) {
# dp[i][0] = (dp[i - 1][ 0] % m + dp[i - 1][ 1] % m + dp[i - 1][ 2] % m) % m;// s
# dp[i][1] = (dp[i - 1][ 0] % m + dp[i - 1][ 2] % m) % m; // p
# dp[i][2] = (dp[i - 1][ 0] % m + dp[i - 1][ 1] % m - 2 * dp[i - 2][ 2] % m + m) % m; // T

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        m = 1000000007
        dp = [[0 for x in range(3)] for y in range(int(A+1))]
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1
        dp[2][0] = 3
        dp[2][1] = 2
        dp[2][2] = 2
        print(dp)
        for i in range(2, A + 1):
            dp[i][0] = (dp[i - 1][0] % m + dp[i - 1][1] % m + dp[i - 1][2] % m) % m
            dp[i][1] = (dp[i - 1][0] % m + dp[i - 1][2] % m) % m
            print("dp[i - 2][2]", dp[i - 2][2])
            dp[i][2] = (dp[i - 1][0] % m + dp[i - 1][1] % m - 2 * dp[i - 2][2] % m + m) % m
        print(dp)
        return int(((dp[A][0] + dp[A][1] + dp[A][2]) % m))


A = 2
A = 3
s = Solution()
print(s.solve(A))
