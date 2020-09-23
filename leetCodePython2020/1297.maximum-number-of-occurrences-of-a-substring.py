#
# @lc app=leetcode id=1297 lang=python3
#
# [1297] Maximum Number of Occurrences of a Substring
#

# @lc code=start


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        counter = collections.Counter()

        # only check the mini size since anything
        # addition to that will also cover the mini size
        for i in range(len(s)-minSize+1):
            temp = s[i:i+minSize]
            if len(set(temp)) <= maxLetters:
                counter[temp] += 1
        return max(counter.values()) if counter else 0

# @lc code=end
