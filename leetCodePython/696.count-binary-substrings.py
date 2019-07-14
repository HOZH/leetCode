#
# @lc app=leetcode id=696 lang=python
#
# [696] Count Binary Substrings
#


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        current = s[0]

        current_count = 0

        storage = list()

        for i in s:
            if i == current:
                current_count += 1

            else:
                current = i
                storage.append(current_count)
                current_count = 1

        storage.append(current_count)

        result = 0

        for i in range(len(storage)-1):

            result += storage[i] if storage[i] < storage[i+1] else storage[i+1]

        return result
