#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zero_count = arr.count(0)
        if zero_count > 1:
            return True
        temp = set(arr)-{0}
        zero_count = arr.count(0)

        for i in arr:
            if i*2 in temp:
                return True
        return False

# @lc code=end
