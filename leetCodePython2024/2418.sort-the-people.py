#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined_list = []
        for i in range(len(names)):
            combined_list.append((names[i], heights[i]))

        combined_list.sort(key=lambda x: x[1],reverse=True)
        return list(map(lambda x: x[0], combined_list))

# @lc code=end
