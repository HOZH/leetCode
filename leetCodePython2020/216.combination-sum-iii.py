#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        self.ans = []
        candidates = [i for i in range(1, 10)]
        target = n

        def helper(start_index, current_list, current_target, count):

            current_sum = sum(current_list)
            if count > k:
                return

            if current_sum == target:
                if count == k:
                    self.ans.append(current_list)
                # always return no matter value of count
                return
            elif current_sum > target:
                return
            for i in range(start_index, len(candidates)):

                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > current_target:
                    break

                helper(i+1, current_list+[candidates[i]],
                       current_target-candidates[i], count+1)

        helper(0, [], target, 0)
        return self.ans

# @lc code=end
