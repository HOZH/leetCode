#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:

        if not len(s):
            return ''

        chars = [*s]
        pre = ord(chars[0])
        index = 1

        while index < len(chars):

            current_ord = ord(chars[index])

            if abs(pre-current_ord) == 32:
                pre = ord(chars[index-2]) if (index-2) >= 0 else 1000
                chars = chars[:index-1]+chars[index+1:]
                index -= 1
                if index == 0:
                    if not len(chars):
                        return ''

                    index += 1
                    pre = ord(chars[0])
                continue

            pre = current_ord
            index += 1

        return ''.join(chars)
# @lc code=end
