#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        if not len(target):
            return []
        current = 1
        tail = target[-1]

        result = []
        target
        while current <= tail:
            result.append('Push')

            if current not in target:
                result.append('Pop')

            current += 1

        return result


# @lc code=end
