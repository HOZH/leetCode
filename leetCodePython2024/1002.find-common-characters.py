#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # 'abb' => Counter(['a'=1, 'b'=2])
        # ["bella","label","roller"]
        # [{b: 1, e: 1, l:2, a:1}, {b: 1, e: 1, l:2, a:1}, ...]
        counters = list(map(lambda x: Counter(x), words))
        # reduce means lambda x,y: x+y. .... reduce([1,2])=>3
        reduced_counter = reduce(lambda x, y: x & y, counters)

        return list(reduced_counter.elements())

        # old solution

        chars_in_words = list(map(lambda x: set([*x]), words))
        if not len(chars_in_words):
            return []
        common_chars = chars_in_words[0]
        for i in range(1, len(chars_in_words)):
            common_chars &= chars_in_words[i]

        ans = []
        common_chars = list(common_chars)
        common_chars.sort()
        for i in common_chars:
            char_count = 10e5
            for j in words:
                char_count = min(j.count(i), char_count)

            ans.extend([i]*char_count)

        return ans


# @lc code=end



 def commonChars(self, words: List[str]) -> List[str]:
        char_dict = {}
        output = []

        for word in words:
            for char in word:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
        
        total_words = len(words)
        print('total words: ', total_words)
        print('char_dict', char_dict)
        """
        """

        for key, value in char_dict.items():
            if value >= total_words:
                # remainder = value % total_words
                total_chars = value // total_words
                while total_chars > 0:
                    output.append(key)
                    total_chars -= 1
                # if remainder == 0:
                #     output.append(key)
        
        return output

['ll','l','a']
["bella","label","roller"]
total words:  3
char_dict {'b': 2, 'e': 3, 'l': 6, 'a': 2, 'r': 2, 'o': 1}

["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
total words:  8
char_dict {'a': 14, 'c': 19, 'b': 13, 'd': 18}