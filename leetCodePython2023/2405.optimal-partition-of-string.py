#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        result_lis = []
        current_sub_string = ''
        current_char_set = set()

        for i in s:
            if i in current_char_set:
                result_lis.append(current_sub_string)
                current_sub_string = i
                current_char_set = set([i])
            else:
                current_char_set.add(i)
                current_sub_string += i

        return len(result_lis) + (1 if len(current_sub_string) else 0)

# @lc code=end
