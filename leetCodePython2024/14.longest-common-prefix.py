#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ''
        strs.sort(key=len)
        validator = strs[0]
        rest_of_strs = strs[1:]
        for i in range(len(validator), 0, -1):
            current_validator = validator[:i]
            is_current_validator_valid = True
            for string in rest_of_strs:
                if not string.startswith(current_validator):
                    is_current_validator_valid = False
                    break
            if is_current_validator_valid:
                return current_validator

        return ''


# @lc code=end
