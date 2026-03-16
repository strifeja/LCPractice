class Solution {
public:
    int climbStairs(int n) {
        // Base case, if n is less than or equal to 2 return n
        if (n <= 2) {
            return n;
        }

        // Initialize dynamic programming array:
        // dp[1] represents all possibilities of 1
        // dp[2] represents all possibilities of 2
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;

        // Iterate from 3 to n
        // Example:
        //      dp[3] = 2 + 1;
        //      dp[4] = 3 + 2;
        //      dp[5] = 5 + 3;
        //      dp[6] = 8 + 4;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n];
    }
};