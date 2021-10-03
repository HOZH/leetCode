#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        mapping = {x: str(ord(x)-97) for x in list(map(chr, range(97, 123)))}

        first_val = int(''.join(list(map(lambda x: mapping[x], firstWord))))
        sec_val = int(''.join(list(map(lambda x: mapping[x], secondWord))))
        target_val = int(''.join(list(map(lambda x: mapping[x], targetWord))))

        return target_val== sec_val+first_val


# @lc code=end
