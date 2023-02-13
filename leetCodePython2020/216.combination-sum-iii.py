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

        def helper(start_index, current_list, current_target, count):
            if count > k:
                return
            current_sum = sum(current_list)

            if current_sum == n:
                if count == k:
                    self.ans.append(current_list)
                # always return no matter value of count
                return
            elif current_sum > n:
                return
            for i in range(start_index, len(candidates)):
                if candidates[i] > current_target:
                    break

                helper(i+1, current_list+[candidates[i]],
                       current_target-candidates[i], count+1)

        helper(0, [], n, 0)
        return self.ans

# @lc code=end
