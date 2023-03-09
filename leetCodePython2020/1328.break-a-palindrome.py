#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        def helper(index):
            left, right = palindrome[:index], palindrome[index+1:]
            if left == right:
                return ''
            prev = palindrome[index]
            return left+('a' if prev != 'a' else 'b')+right

        length = len(palindrome)
        if length == 1:
            return ''
        ans = 'z'*length
        for i in range(length):
            temp = helper(i)
            if len(temp) > 0:
                ans = min(ans, helper(i))
        return ans


# @lc code=end
