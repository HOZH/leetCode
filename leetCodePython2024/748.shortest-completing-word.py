#
# @lc app=leetcode id=748 lang=python3
#
# [748] Shortest Completing Word
#

# @lc code=start
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        counter = Counter(map(lambda y: y.lower(), filter(
            lambda x: x.isalpha(), [*licensePlate]))).items()
        qualified_words = set()

        def helper(word) -> int:
            for key, count in counter:
                if word.count(key) < count:
                    return 1001
            qualified_words.add(word)
            return len(word)

        word_len_list = list(map(lambda x: (helper(x), x), words))

        # double pass to get first min length answer
        min_len = min(word_len_list)[0]

        for i in words:
            if i in qualified_words and len(i) == min_len:
                return i


# @lc code=end
def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hashmap = {}
        shortest_word_len = float('inf')
        earliest_index = float('inf')
        output = ''

        for char in licensePlate:
            if not char.isalpha():
                continue

            key = char.lower()
            if key in hashmap:
                hashmap[key] += 1
            else:
                hashmap[key] = 1
        
        for index, word in enumerate(words):
            curr_hash = hashmap

            for char in word:
                if char in curr_hash:
                    if curr_hash[char] > 0:
                        curr_hash[char] -= 1
                    else:
                        break

            if sum(curr_hash.values()) == 0:
                curr_word_len = len(word)

                if index < earliest_index and curr_word_len < shortest_word_len:
                    earliest_index = index
                    shortest_word_len = curr_word_len
                    output = word
            
        return output
                
