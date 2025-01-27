#
# @lc app=leetcode id=3340 lang=python3
#
# [3340] Check Balanced String
#

# @lc code=start
class Solution:
    def isBalanced(self, num: str) -> bool:
        even, odd = 0, 0
        for i in range(len(num)):
            current = int(num[i])
            if i % 2 == 0:
                even += current
            else:
                odd += current
                
        return even == odd

# @lc code=end
