#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = []
        name_index_pair = dict()
        for index, name in enumerate(names):
            name_index_pair[index] = name
        for i in enumerate(heights):
            temp.append(i)
        temp.sort(key=lambda x: x[1], reverse=True)
        return list(map(lambda x: name_index_pair[x[0]], temp))

# @lc code=end
