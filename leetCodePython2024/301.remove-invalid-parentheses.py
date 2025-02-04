#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
from functools import lru_cache


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        self.ans = []
        self.not_letters = set()

        @lru_cache(None)
        def is_valid(temp):
            left, right = 0, 0
            for i in range(len(temp)):
                if temp[i] == '(':
                    left += 1
                elif temp[i] == ')':
                    right += 1
                if right > left:
                    return False
            return True if left == right else False

        temp_s = ''
        adding_l = False
        # trim ending (
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                adding_l = True
            else:
                if s[i] == '(':
                    if not adding_l:
                        continue
            temp_s = s[i] + temp_s
        s = temp_s

        temp_s = ''
        adding_r = False
        # trim leading )
        for i in range(len(s)):
            if s[i] == '(':
                adding_r = True
            else:
                if s[i] == ')':
                    if not adding_r:
                        continue
            temp_s = temp_s + s[i]
        s = temp_s

        def dfs(current_string: str, start_index, l_count_to_delete, r_count_to_delete):
            if l_count_to_delete == 0 and r_count_to_delete == 0:
                if is_valid(current_string):
                    self.ans.append(current_string)
                return

            for i in range(start_index, len(current_string)):
                # only pick first ele if there're consecutive identical eles
                if i != start_index and current_string[i - 1] == current_string[i]:
                    continue

                current_char = current_string[i]

                temp_string = current_string[:i] + current_string[i + 1:]
                if current_char == '(':
                    dfs(temp_string, i, l_count_to_delete - 1, r_count_to_delete)
                elif current_char == ')':
                    dfs(temp_string, i, l_count_to_delete, r_count_to_delete-1)

        l, r = 0, 0

        for ch in s:
            l += ch == '('
            if l == 0:
                r += ch == ')'
            else:
                l -= ch == ')'

        dfs(s, 0, l, r)
        return self.ans
        
# @lc code=end

