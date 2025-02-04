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

        def helper(start_index, current_list,):
            current_sum = sum(current_list)
            if current_sum == n and len(current_list) == k:
                self.ans.append(current_list)
                return
            elif current_sum > n or len(current_list) > k:
                return

            for i in range(start_index, len(candidates)):
                if candidates[i] > n-current_sum:
                    break

                helper(i+1, current_list+[candidates[i]],)

        helper(0, [],)
        return self.ans

# @lc code=end
