#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        n = len(nums)
        d = 2**32
        ans = 0 * n
        for i in range(n-2):
            s, t = i+1, n-1
            while s < t:
                curr = nums[i]+nums[s]+nums[t]
                if curr == target:
                    return target
                diff = abs(curr-target)
                if diff < d:
                    d = diff
                    ans = curr
                if curr > target:
                    t -= 1
                else:
                    s += 1

        return ans

# @lc code=end
