#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        candidates = [i for i in range(1, n+1)]

        # def helper(start_index, current_list, current_count):
        #     if current_count == k:
        #         self.ans.append(current_list)
        #         return
        #     for i in range(start_index, len(candidates)):
        #         helper(i+1, current_list+[candidates[i]],
        #                current_count+1)

        # helper(0, [], 0)
        def c(nums, depth, start_index, current_list):

            if depth == k:
                # ans.append(current_list)
                self.ans.append(current_list[:])
                return

            for i in range(start_index, len(nums)):
                current_list.append(nums[i])
                c(nums, depth+1, i+1, current_list)
                current_list.pop()

        c(candidates, 0, 0, [])
        return self.ans

# @lc code=end
