#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        temp = chars[:]
        ans = 0


        for word in words:

            temp = chars[:]

            formed = True
            for i in word:
                if i in temp:
                    temp = temp.replace(i, '', 1)
                else:
                    formed = False
                    break

            if formed:
                ans += len(word)

        return ans


# @lc code=end
