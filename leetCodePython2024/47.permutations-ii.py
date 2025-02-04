#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        target_count = len(nums)
        nums.sort()
        used = [False]*len(nums)

        def helper(nums, depth, current_list, ans):

            if depth == target_count:
                ans.append(current_list)
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    # used[i-1] implies prev identical num has been used in the
                    # given context since nums[i] == nums[i-1]
                    # this operation require a sorted nums
                    # used i-1 == false means prev identical num was not selected
                    # therefore the current num should also be skipped as well
                    continue

                used[i] = True
                helper(nums, depth+1,
                       current_list+[nums[i]], ans)
                used[i] = False

        helper(nums, 0,  [], self.ans)
        return self.ans

# @lc code=end
