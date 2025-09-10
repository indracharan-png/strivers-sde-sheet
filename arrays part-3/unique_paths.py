class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize 2d dp array
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Set up the Basecases, all the below cells have only one possible way from them to finish cell
        for j in range(n):
            dp[m-1][j] = 1
        for i in range(m):
            dp[i][n-1] = 1
        
        # Iterate over DP array in bottom up approach (finsh -> start)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                # Each cell has two possible moves (dowm & right), add up the total plausible moves
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        # Top-left cell will have all the ways to reach bottom-right
        return dp[0][0]
        