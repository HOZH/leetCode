#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # assaume there's duplicate eles
        # pool = dict()
        # for i in range(len(nums)):
        #     current = nums[i]
        #     if current not in pool:
        #         pool[current] = set([i])
        #     else:
        #         pool[current].add(i)

        #     if target - current in pool:

        #         current_set = pool[target-current]

        #         temp_set = set()
        #         while len(current_set):
        #             temp = current_set.pop()
        #             if temp != i:
        #                 return [i, temp]
        #             temp_set.add(temp)
        #         pool[target-current] = temp_set

        pool = dict()

        for i in range(len(nums)):
            if nums[i] in pool:
                return [pool[nums[i]], i]
            else:
                pool[target-nums[i]] = i

# @lc code=end
