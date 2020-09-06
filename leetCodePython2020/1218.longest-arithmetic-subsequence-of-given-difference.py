#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start

from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        temp = defaultdict(int)
        for i in range(len(arr)-1, -1, -1):
            temp[arr[i]] = temp[arr[i]+difference]+1
        return max(temp.values())


# @lc code=end
