#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        def c(nums, target_count, depth, start_index, current_list, ans):

            if target_count == depth:
                ans.append(''.join(current_list))
                return

            for i in range(start_index, len(nums)):
                # current_list.append(nums[i])
                c(nums, target_count, depth+1,
                  i+1, current_list+[nums[i]], ans)
                # current_list.pop()

        self.ans = []
        c([*characters], combinationLength, 0, 0, [], self.ans)

        self.ans.sort()

    def next(self) -> str:

        return self.ans.pop(0)

    def hasNext(self) -> bool:

        return len(self.ans) > 0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
