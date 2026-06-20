#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        s_len = len(s)
        t_len = len(t)
        # starting index in t to check for remaining chars in s
        t_pointer = 0

        for s_index in range(s_len):
            current_s = s[s_index]
            # flag to determine if we found the current char in s in t after
            # iterated through (t_pointer, t_len -1) in t
            found_next_char = False
            # early return if length of remaining chars in t is less than
            # length of reamining chars in s
            if (t_len - t_pointer) < (s_len - s_index):
                return False
            
            for t_index in range(t_pointer,t_len):
                current_t = t[t_index]
                if current_t == current_s:
                    if s_index == (s_len -1):
                        return True
                    else:
                        # check next char in s
                        t_pointer = t_index + 1
                        found_next_char = True
                        break
            if not found_next_char:
                return False
        return False
        
# @lc code=end

