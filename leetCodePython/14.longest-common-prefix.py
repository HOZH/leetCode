#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        length = len(strs)
        if length == 0:
            return ""
        if length == 1:
            return strs[0]

        flag = min(strs)
        count = 0

        for i in range(len(flag)):

            if all(x[i] == flag[i] for x in strs):

                count += 1

            else:
                break

        return flag[:count]
