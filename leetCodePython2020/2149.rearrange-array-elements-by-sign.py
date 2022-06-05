#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative, positive = [], []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result


# @lc code=end
