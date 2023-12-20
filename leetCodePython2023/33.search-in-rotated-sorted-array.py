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
            return 0 if nums[0]==target else -1
        l, r = 0, length-1

        while l < r:

            pivot = l+(r-l)//2

            if nums[pivot] == target:
                return pivot

            if nums[l] < nums[pivot]:
                # l arr sorted
                # bs l

                local_l, local_r = l, pivot

                while local_l < local_r:

                    local_pivot = local_l+(local_r-local_l)//2

                    if nums[local_pivot] == target:
                        return local_pivot

                    elif nums[local_pivot] > target:
                        local_r = local_pivot
                    else:
                        local_l = local_pivot+1
                # not found, searching global right arr instead
                l = pivot

            else:
                # left arr not sorted => right arr sorted
                local_l, local_r = pivot+1, r+1

                while local_l < local_r:

                    local_pivot = local_l+(local_r-local_l)//2

                    if nums[local_pivot] == target:
                        return local_pivot
                    elif nums[local_pivot] > target:
                        local_r = local_pivot
                    else:
                        local_l = local_pivot+1

                r = pivot 

        return -1
