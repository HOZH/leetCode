#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        length = len(nums)
        if not length:
            return -1

        l, r = 0, length-1

        while l <= r:

            pivot = l+(r-l)//2
            current = nums[pivot]

            if current == target:
                return pivot

            elif current < target:

                l = pivot+1

            else:
                r = pivot-1

        return -1

    # def search_temp(self, nums: List[int], target: int) -> int:

    #     length = len(nums)
    #     if length == 0:
    #         return -1

    #     l, r = 0, length-1

    #     while l < r:

    #         m = l + (r-l)//2

    #         current = nums[m]

    #         if current == target:
    #             return m

    #         elif current > target:
    #             r = m-1

    #         else:
    #             l = m+1

    #     return l if nums[l] == target else -1

# @lc code=end
