#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.ans = []
        self.target_count = len(nums)

        def p(nums, depth, used, current_list):
            if depth == self.target_count:
                self.ans.append(current_list)
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                p(nums, depth+1, used, current_list+[nums[i]])
                used[i] = False

        p(nums, 0, [False]*self.target_count, [])

        return self.ans

# @lc code=end

