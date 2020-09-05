#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        def helper(nums, target_count, depth, used, current_list, ans):

            if target_count == depth:
                ans.append(current_list)
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    # used[i-1] implies prev identical num has been used in given
                    # context since nums[i] == nums[i-1]
                    # this operation require a sorted nums
                    # used i-1 == false means prev identical num was not selected
                    # therefore the current num should also be skipped as well
                    continue

                used[i] = True
                helper(nums, target_count, depth+1,
                       used, current_list+[nums[i]], ans)
                used[i] = False

        helper(nums, len(nums), 0, [False]*len(nums), [], self.ans)
        return self.ans

# @lc code=end
