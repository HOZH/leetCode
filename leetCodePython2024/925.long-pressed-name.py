#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1, p2 = 0, 0
        while p2 < len(typed):
            # if name[p1] == typed[p2]: proceed to next char in both name and typed
            if p1 < len(name) and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            # if name[p1] != typed[p2] but typed[p2] is the same as previous char in typed (long pressed), proceed to next char in typed
            elif p2 != 0 and typed[p2] == typed[p2-1]:
                p2 += 1
            # typed[p2] is neither long pressed nor the same as name[p1], return False
            else:
                return False
        # return True
        # cannot just return True
        """
        alexd
        ale
        could fail after p2 = len(typed) since p1 is not at the end of name yet
        """
        return p1 == len(name)

        def get_non_dup_chars_and_substr_count(content):
            len_for_each_substr = []
            non_dup_chars = []
            current_char = None
            current_counter = 0
            for i in content:
                if i == current_char:
                    current_counter += 1
                elif current_char is None:
                    current_char = i
                    current_counter = 1
                else:
                    if current_char is not None:
                        len_for_each_substr.append(current_counter)
                        non_dup_chars.append(current_char)

                        current_char = i
                        current_counter = 1

            len_for_each_substr.append(current_counter)
            non_dup_chars.append(current_char)

            return non_dup_chars, len_for_each_substr

        non_dup_chars_typed, len_for_each_substr_typed = (
            get_non_dup_chars_and_substr_count(typed)
        )
        non_dup_chars_name, len_for_each_substr_name = (
            get_non_dup_chars_and_substr_count(name)
        )
        if non_dup_chars_name != non_dup_chars_typed:
            return False

        for i in range(len(len_for_each_substr_name)):
            if len_for_each_substr_typed[i] < len_for_each_substr_name[i]:
                return False

        return True


# @lc code=end

name = "alex"
typed = "aaleex a"

def isLongPressedName(self, name: str, typed: str) -> bool:
        n = 0
        t = 0
        while n < len(name) and t < len(typed):
            char_name = name[n]
            char_typed = typed[t]
            if char_name == char_typed:
                n += 1
                t += 1
            else:
                while t < len(typed) and typed[t] != char_name:
                    t += 1
                if t >= len(typed):
                    return False
        
        if n < len(name):
            return False
        if n < len(name) and t < len(typed):
            if typed[t] != name[n]:
                return False
        return True