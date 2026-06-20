#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(original_str):
            char_mapping = dict()
            result = ''
            for i, char in enumerate(original_str):
                if char not in char_mapping:
                    char_mapping[char] = '|'+str(i)+'|'
                result += char_mapping[char]
            return result
        return helper(s) == helper(t)
                
        
# @lc code=end

