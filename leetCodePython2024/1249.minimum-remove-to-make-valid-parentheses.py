#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_count, right_count = 0, 0
        left_filtered_str = ''
        for i in s:
            if i == '(':
                left_count += 1
                left_filtered_str += i
            elif i != ')':
                left_filtered_str += i
            else:
                if left_count > right_count:
                    right_count += 1
                    left_filtered_str += i
        answer = ''
        left_count = 0
        for i in left_filtered_str:
            if i != '(':
                answer += i
            else:
                if left_count < right_count:
                    left_count += 1
                    answer += i

        return answer


# @lc code=end
