#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        self.ans = []
        candidates.sort()
        def helper(start_index, current_list, current_target):

            current_sum = sum(current_list)

            if current_sum == target:
                self.ans.append(current_list)
                return
            elif current_sum > target:
                return
            for i in range(start_index, len(candidates)):

                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > current_target:
                    break

                helper(i+1, current_list+[candidates[i]],
                       current_target-candidates[i])

        helper(0, [], target)
        return self.ans

        # @lc code=end
