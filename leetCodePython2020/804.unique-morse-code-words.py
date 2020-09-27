#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        temp_set = set()
        for s in words:
            temp_morse = ''
            for i in range(len(s)):
                temp_morse += morse[ord(s[i])-97]

            temp_set.add(temp_morse)

        return len(temp_set)

# @lc code=end
