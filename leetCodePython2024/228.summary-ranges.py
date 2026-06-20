#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        def get_sub_range(start, end):
            if start == end:
                return str(start)
            else:
                return str(start)+'->'+str(end)

        head, prev = None, None
        result = []
        for i in nums:
            if prev is None:
                head = i
            elif i == prev+1:
                pass
            else:
                result.append(get_sub_range(head, prev))
                head = i
            prev = i
        # last iteration on previous loop won't append the sub range to result
        result.append(get_sub_range(head, prev))

        return result


# @lc code=end
