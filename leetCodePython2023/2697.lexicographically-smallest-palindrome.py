#
# @lc app=leetcode id=2697 lang=python3
#
# [2697] Lexicographically Smallest Palindrome
#

# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        temp = [*s]
        length = len(s)
        for i in range(length//2):
            head, tail = temp[i],temp[-(i+1)]
            if head != tail:
                print(True)
                if head<tail:
                    temp[-(i+1)]=head
                else:
                    temp[i]=tail
        
        return ''.join(temp)
        
# @lc code=end

