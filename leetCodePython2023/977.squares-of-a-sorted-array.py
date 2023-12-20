#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        negatives, non_negatives = [], []
        for i in nums:
            temp = i**2
            if i < 0:
                negatives = [temp]+negatives
            else:
                non_negatives = non_negatives+[temp]

        ans = []
        while len(negatives) and len(non_negatives):
            if negatives[0] < non_negatives[0]:
                ans.append(negatives[0])
                negatives = negatives[1:]
            else:
                ans.append(non_negatives[0])
                non_negatives = non_negatives[1:]

        if len(negatives):
            ans.extend(negatives)
        elif len(non_negatives):
            ans.extend(non_negatives)

        return ans

# @lc code=end
