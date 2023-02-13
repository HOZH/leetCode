#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def is_possible(threshold):
            count = 1
            total = 0
            for n in nums:
                total+=n
                if total>threshold:
                    count+=1
                    total=n
                if count>k:
                    return False
            return True
                
        l, r = max(nums), sum(nums)

        while l < r:
            m = l + (r-l)//2
            if is_possible(m):
                r = m
            else:
                l = m+1
        return l

# @lc code=end
