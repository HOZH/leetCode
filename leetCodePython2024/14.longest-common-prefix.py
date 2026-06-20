#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

["flower","flower","flour"]
["racecar","dog","car"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        if  len(strs) == 1:
            return first_word
        
        ans = ''
        for current_char_index in range(len(first_word)):
            current_char = first_word[current_char_index]
            for word in strs[1:]:
                if len(word) <= current_char_index or word[current_char_index] !=current_char:
                    # return first_word[:current_char_index]
                    return ans
            ans += current_char
        return first_word


# @lc code=end


def longestCommonPrefix(self, strs):

        n=len(strs)
        IsCommonChar=False
        if n==0:
            return ""

        Temp=""    
        First_Word=strs[0]

        for i in range(len(First_Word)):
            char=First_Word[i]
            for j in range(1,n):
                if i >= len(strs[j]) or char != strs[j][i]:
                    return Temp

            Temp+=char    


        return Temp   