#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        while True:

            if len(ransomNote) == 0:
                break

            current = ransomNote[0]

            if magazine.__contains__(current):

                magazine=magazine.replace(current,'',1)
                
                ransomNote=ransomNote[1:]

            else:
                
                return False


        return True

            
        

