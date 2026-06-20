#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = dict()
        for i in range(len(nums)):
            current_num = nums[i]
            if current_num in index_map and i - index_map[current_num] <= k:
                    return True
            index_map[current_num]  = i
        
        return False
        
        
# @lc code=end

