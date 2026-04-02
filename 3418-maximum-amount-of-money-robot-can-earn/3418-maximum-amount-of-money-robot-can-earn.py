class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        
        NEG_INF = float('-inf')
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        
        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = max(coins[0][0], 0) 
        dp[0][0][2] = 0 
        
        for j in range(1, n):
            v = coins[0][j]
            for k in range(3):
                if dp[0][j-1][k] == NEG_INF:
                    continue
                dp[0][j][k] = max(dp[0][j][k], dp[0][j-1][k] + v)
                if v < 0 and k < 2:
                    dp[0][j][k+1] = max(dp[0][j][k+1], dp[0][j-1][k])
        
        for i in range(1, m):
            v = coins[i][0]
            for k in range(3):
                if dp[i-1][0][k] == NEG_INF:
                    continue
                dp[i][0][k] = max(dp[i][0][k], dp[i-1][0][k] + v)
                if v < 0 and k < 2:
                    dp[i][0][k+1] = max(dp[i][0][k+1], dp[i-1][0][k])
        
        for i in range(1, m):
            for j in range(1, n):
                v = coins[i][j]
                for k in range(3):
                    best = max(
                        dp[i-1][j][k] if dp[i-1][j][k] != NEG_INF else NEG_INF,
                        dp[i][j-1][k] if dp[i][j-1][k] != NEG_INF else NEG_INF
                    )
                    if best == NEG_INF:
                        continue
                    dp[i][j][k] = max(dp[i][j][k], best + v)
                    if v < 0 and k < 2:
                        dp[i][j][k+1] = max(dp[i][j][k+1], best)
        
        return max(dp[m-1][n-1])