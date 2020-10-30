#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start


class Solution:
    def diStringMatch(self, S: str) -> List[int]:

        lo, hi = 0, len(S)
        result = []

        for i in S:
            if i == 'I':
                result.append(lo)
                lo += 1
            else:
                result.append(hi)
                hi -= 1

        return result+[lo]


# @lc code=end
