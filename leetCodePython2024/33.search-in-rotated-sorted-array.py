#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 1:
            return 0 if nums[0] == target else -1
        l, r = 0, length-1

        while l < r:
            pivot = l+(r-l)//2

            if nums[l] >= nums[pivot]:
                # left arr not sorted => right arr sorted
                local_l, local_r = pivot+1, r
                while local_l < local_r:
                    local_pivot = local_l+(local_r-local_l)//2
                    if nums[local_pivot] >= target:
                        local_r = local_pivot
                    else:
                        local_l = local_pivot+1

                if nums[local_l] == target:
                    return local_l
                r = pivot

            else:
                # l arr sorted
                # bs l

                local_l, local_r = l, pivot
                while local_l < local_r:
                    local_pivot = local_l+(local_r-local_l)//2
                    if nums[local_pivot] >= target:
                        local_r = local_pivot
                    else:
                        local_l = local_pivot+1
                if nums[local_l] == target:
                    return local_l
                # not found, searching global right arr instead
                l = pivot+1

        return l if nums[l] == target else -1

# @lc code=end
