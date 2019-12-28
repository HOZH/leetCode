#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)

        if length == 0:
            return 0
        if length == 1:
            return 1
        max_count = 0
        count, chars = 0, dict()

        stop_pt = 0
        for i in range(length):

            current = s[i]

            if current in chars:

                if count > max_count:
                    max_count = count

                if chars[current] < stop_pt:
                    continue

                count = i - chars[current]

                chars[current] = i
                stop_pt = i
                continue

            chars[current] = i
            count += 1

        return count if count > max_count else max_count

