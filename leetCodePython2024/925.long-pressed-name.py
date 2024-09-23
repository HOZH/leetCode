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
            if p1 < len(name) and name[p1] == typed[p2]:
                p1 += 1
                p2 += 1
            elif p2 != 0 and typed[p2] == typed[p2-1]:
                p2 += 1
            else:
                return False
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
