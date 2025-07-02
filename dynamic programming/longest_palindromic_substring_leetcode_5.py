class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)

        if s_len < 2:
            return s
        
        max_len = 1
        output = s[0]

        # Initialize the 2d DP table
        dp = [[False] * s_len for _ in range(s_len)]

        # Base Case-1: Set the diagonal to true
        for i in range(s_len-1, -1, -1):
            dp[i][i] = True

        # Base Case-2: Update the values of substrings of length 2 (upper diagonal to principal diagonal) 
        for i in range(s_len - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                if max_len < 2:
                    max_len = 2
                    output = s[i:i + 2]

        # Traverse the upper traingle of DP table and update
        deduct = 3
        while(deduct <= s_len):
            for left_idx in range(s_len-deduct, -1, -1):
                right_idx = left_idx + (deduct-1)
                dp[left_idx][right_idx] = (s[left_idx] == s[right_idx]) and (dp[left_idx + 1][right_idx - 1])

                # Check and update the answer
                if(dp[left_idx][right_idx] and right_idx - left_idx + 1 > max_len):
                    max_len = right_idx - left_idx + 1
                    output = s[left_idx: right_idx + 1]
                    
            deduct += 1
        
        return output
        
        

                
            