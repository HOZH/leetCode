#
# @lc app=leetcode id=1961 lang=python3
#
# [1961] Check If String Is a Prefix of Array
#

# @lc code=start
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        s_length = len(s)

        current_len = 0
        current_str = ''

        for i in range(len(words)):
            if i >= s_length:
                return False

            current = words[i]
            current_len += len(current)
            current_str += current

            if not s.startswith(current_str):
                return False

            if current_len >= s_length:
                if current_len > s_length:
                    return False
                else:
                    return current_str == s


# @lc code=end
