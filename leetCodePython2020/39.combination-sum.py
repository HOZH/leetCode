#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # can be boosted up by using heapq
        self.result_set = set()
        candidates.sort()

        def helper(current, t):
            for i in candidates:
                if i == t:
                    self.result_set.add(tuple(sorted(current+[t])))
                elif i < t:
                    if t-i < candidates[0]:
                        continue
                    helper(current+[i], t-i)
                else:
                    break

        helper([], target)
        return sorted(list(self.result_set))


# @lc code=end
