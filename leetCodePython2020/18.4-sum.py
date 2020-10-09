#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        result = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                temp = target-nums[i]-nums[j]

                l, r = j+1, len(nums)-1

                while l < r:

                    if nums[l]+nums[r] == temp:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1

                    elif nums[l]+nums[r] < temp:
                        l += 1
                    else:
                        r -= 1
        return list(map(lambda x: list(x), result))


# @lc code=end
