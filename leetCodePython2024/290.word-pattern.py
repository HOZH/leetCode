#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words)!=len(pattern):
            return False
        # get all unique chars in given pattern, preserve the order of first occurrence
        # pattern = 'abc'
        # list(pattern) = ['a', 'b', 'c']
        # dict.fromkeys(list(pattern)) = {'a': None, 'b': None,}
        # pattern_elements = list(dict.fromkeys(list(pattern))) = ['a', 'b', 'c']
        pattern_elements  = list(dict.fromkeys(list(pattern)))
        pattern_elements_len = len(pattern_elements)
        # counter to keep track how many unique word we have seen in words
        unique_word_count = 0
        mapping = dict()

        for word_index in range(len(words)):
            word = words[word_index]
            
            if word not in mapping:
                # dog cat cat fish
                # abba
                # abbc
                if unique_word_count>=pattern_elements_len:
                    return False

                mapping[word] = pattern_elements[unique_word_count]
                unique_word_count += 1
            else:
                if mapping[word] != pattern[word_index]:
                    return False
        
        return True
        
# @lc code=end

