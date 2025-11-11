class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        num_strings = len(strs)
      
       
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(num_strings + 1)]
      
        for string_idx, current_string in enumerate(strs, 1):
            zeros_count = current_string.count("0")
            ones_count = current_string.count("1")
          
            for zeros_limit in range(m + 1):
                for ones_limit in range(n + 1):
                    dp[string_idx][zeros_limit][ones_limit] = dp[string_idx - 1][zeros_limit][ones_limit]
                  
                    if zeros_limit >= zeros_count and ones_limit >= ones_count:
                        dp[string_idx][zeros_limit][ones_limit] = max(
                            dp[string_idx][zeros_limit][ones_limit],
                            dp[string_idx - 1][zeros_limit - zeros_count][ones_limit - ones_count] + 1
                        )
      
        return dp[num_strings][m][n]

        