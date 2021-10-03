#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        total = 3*2**(n-1)
        if k > total:
            return ''

        chars = set('abc')
        last = ''

        result = ['']*n
        for i in range(n):
            # list of possible letters after the last used one:
            choice = sorted(chars - set(last))
            # how many substrings of length (n-i-1) are possible:
            total //= len(choice)
            # pick the letter at index i:
            last = choice[(k-1)//total]
            result[i] = last
            # reduce k to pick from substrings:
            k %= total

        return ''.join(result)


# @lc code=end
