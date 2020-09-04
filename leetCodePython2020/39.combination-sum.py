#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # can be boosted up by using heapq
        # self.result_set = set()
        # candidates.sort()

        # def helper(current, t):
        #     for i in candidates:
        #         if i == t:
        #             self.result_set.add(tuple(sorted(current+[t])))
        #         elif i < t:
        #             if t-i < candidates[0]:
        #                 continue
        #             helper(current+[i], t-i)
        #         else:
        #             break

        # helper([], target)
        # return sorted(list(self.result_set))

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
                if candidates[i] > current_target:
                    break

                helper(i, current_list+[candidates[i]], target-candidates[i])

        helper(0, [], target)
        return self.ans


# @lc code=end
