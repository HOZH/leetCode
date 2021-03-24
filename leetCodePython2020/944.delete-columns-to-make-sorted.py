#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        length = len(strs)
        if not length:
            return 0

        str_len = len(strs[0])

        temp_arr = [[] for _ in range(str_len)]

        for i in range(str_len):
            for j in range(length):
                temp_arr[i].append(strs[j][i])

        count = sum([0 if sorted(i) == i else 1 for i in temp_arr])
        return count

# @lc code=end
