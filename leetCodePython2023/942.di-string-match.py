#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#

# @lc code=start
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0]*(len(s)+1)
        count = 0
        high = len(s)
        for i in range(len(s)):
            if s[i] == "I":
                ans[i] = count
                count += 1
            else:
                ans[i] = high
                high -= 1
        ans[-1] = count
        return ans


# @lc code=end
