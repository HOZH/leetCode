#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        count = 0
        result = []
        current = ''
        for i in s:
            count += 1
            current += i
            if count == k:
                result.append(current)
                current = ''
                count = 0
        if len(current) != 0:
            current += (k-len(current))*fill
            result += [current]
        return result


# @lc code=end
