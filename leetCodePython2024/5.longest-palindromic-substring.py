#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# from functools import lru_cache
class Solution:
    def longestPalindrome(self, s: str) -> str:

        # s_len = len(s)
        # ans = (0,'')
        # valid = set()
        # def helper(sub_str):
        #     if sub_str in valid:
        #         return True
        #     if sub_str == sub_str[::-1]:
        #         valid.add(sub_str)
        #         return True
            
        #     return False

        # for length in range(1,s_len+1):
        #     for i in range(s_len - length +1):
        #         if helper(s[i:i+length]):
        #             ans = max(ans,( length,s[i:i+length]))
        
        # return ans[1]
        s_len = len(s)
        valid = set()
        valid.add('')
        
        # @lru_cache(None)
        def helper(sub_str):
            # if len(sub_str) == 0:
            #     # print(sub_str)
            #     return True
            if sub_str in valid:
                return True
            if sub_str[0] == sub_str[-1]:
                is_inner_sub_palindrome = helper(sub_str[1:-1])
                if is_inner_sub_palindrome:
                    valid.add(sub_str)
                return is_inner_sub_palindrome

            return False

        for length in range(s_len,0,-1):
            for i in range(s_len - length +1):
                if helper(s[i:i+length]):
                    return s[i:i+length]
        


        
# @lc code=end

