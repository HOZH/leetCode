#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()

        def c(target_count, depth, start_index, current_list):
            if target_count == depth:
                self.ans.append(current_list)
            for i in range(start_index, len(nums)):
                if i != start_index and nums[i] == nums[i-1]:
                    continue
                c(target_count, depth+1, i+1, current_list+[nums[i]])

        # iterating through all possible length within the subset
        for i in range(len(nums)+1):
            c(i, 0, 0, [])

        return self.ans
# @lc code=end
