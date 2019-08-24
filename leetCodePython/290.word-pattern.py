#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        dic = dict()
        words = str.split()

        pattern_set = set()

        len_pattern = len(pattern)

        if len(words) != len_pattern:
            return False

        for i in range(len_pattern):

            current_key = pattern[i]
            current_str = words[i]

            if current_key not in dic:

                if current_str in pattern_set:
                    return False
                dic[current_key] = current_str

                pattern_set.add(current_str)

            elif dic[current_key] != current_str:

                return False

        return True
