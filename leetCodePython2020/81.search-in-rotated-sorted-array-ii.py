#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start


class Solution:

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) < 1:
            return False
        pre = nums[0]
        temp = [pre]
        for i in range(1, len(nums)):
            if nums[i] == pre:
                continue

            else:
                temp.append(nums[i])
                pre = nums[i]

        nums = temp
        print(nums)

        length = len(nums)
        l, r = 0, length - 1

        while l <= r:

            pivot = l + (r - l) // 2

            if nums[pivot] == target:
                return True

            # if target<=nums[pivot]:

            if nums[l] < nums[pivot]:
                # l arr sorted
                # bs l

                local_l, local_r = l, pivot - 1

                while local_l <= local_r:

                    local_pivot = local_l + (local_r - local_l) // 2

                    if nums[local_pivot] == target:
                        return True

                    elif target <= nums[local_pivot]:
                        local_r = local_pivot - 1
                    else:
                        local_l = local_pivot + 1
                # not found, searching global right arr instead
                l = pivot + 1

            else:
                # left arr not sorted => right arr sorted
                local_l, local_r = pivot + 1, r

                while local_l <= local_r:

                    local_pivot = local_l + (local_r - local_l) // 2

                    if nums[local_pivot] == target:
                        return True

                    elif target <= nums[local_pivot]:
                        local_r = local_pivot - 1
                    else:
                        local_l = local_pivot + 1

                r = pivot - 1

        return False


# @lc code=end
