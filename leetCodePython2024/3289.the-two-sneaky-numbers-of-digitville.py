#
# @lc app=leetcode id=3289 lang=python3
#
# [3289] The Two Sneaky Numbers of Digitville
#

# @lc code=start
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        encountered = set()
        ans = []
        for i in nums:
            if i not in encountered:
                encountered.add(i)
            else:
                ans.append(i)

        return ans

# @lc code=end
