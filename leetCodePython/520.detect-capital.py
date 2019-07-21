#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
class Solution:
    def detectCapitalUse(self, word: str) -> bool:



        
        return True if (word==word.capitalize() or word == word.lower() or word == word.upper()) else False

        

