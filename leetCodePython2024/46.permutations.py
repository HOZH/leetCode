#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        candidates = sorted(nums)
        k = len(candidates)
        used = [False]*k

        def p(nums, depth, current_list):

            if depth == k:
                self.ans.append(current_list[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_list.append(nums[i])
                    p(nums, depth+1, current_list)
                    current_list.pop()
                    used[i] = False

        p(candidates, 0, [])
        return self.ans

# @lc code=end
