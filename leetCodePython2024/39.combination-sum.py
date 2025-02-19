#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum1(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
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
        # return list(self.result_set)

        self.ans = []
        # candidates.sort()

        def helper(start_index, current_list, current_target):
            current_sum = sum(current_list)
            if current_sum == target:
                self.ans.append(current_list)
                return
            elif current_sum > target:
                return

            for i in range(start_index, len(candidates)):
                if candidates[i] > current_target:
                    # break
                    continue

                helper(i, current_list+[candidates[i]], target-candidates[i])

        helper(0, [], target)
        return self.ans

# @lc code=end
