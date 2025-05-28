#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        bag = {}
        for index, value in enumerate(sorted_scores):
            if index == 0:
                bag[value] = "Gold Medal"
            elif index == 1:
                bag[value] = "Silver Medal"
            elif index == 2:
                bag[value] = "Bronze Medal"
            else:
                bag[value] = str(index + 1)

        return list(map(lambda x: bag[x], score))


# @lc code=end
