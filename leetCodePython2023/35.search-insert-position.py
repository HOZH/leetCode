#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def condition(val):
            return True if val >= target else False
        length = len(nums)
        if length == 1:
            return 0 if target <= nums[0] else 1
        # https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
        l, r = 0, length
        while l < r:
            m = l+(r-l)//2
            if condition(nums[m]):
                r = m
            else:
                l = m+1
        # after exiting the while loop, left is the minimal k​ satisfying the condition function;
        return l


# @lc code=end
