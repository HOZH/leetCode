#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        candidates = sorted(nums)

        def c(nums, depth, start_index, current_list, k):
            if depth == k:
                self.ans.append(current_list[:])
                return

            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                current_list.append(nums[i])
                c(nums, depth+1, i+1, current_list, k)
                current_list.pop()

        for i in range(len(nums)+1):
            c(candidates, 0, 0, [], i)
        return self.ans

# @lc code=end
