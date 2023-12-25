#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.target_count = k

        def c(nums, depth, start_index, current):

            if depth == self.target_count:
                self.ans.append(current)
                return

            for i in range(start_index, len(nums)):
                c(nums, depth+1, i+1, current+[nums[i]])

        c([i for i in range(1, n+1)], 0, 0, [])
        return self.ans

# @lc code=end
