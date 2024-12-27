

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1, len_word2 = len(word1), len(word2)
        self.ans = ''
        for i in range(min(len_word1, len_word2)):
            self.ans += word1[i]+word2[i]

        if len_word1 == len_word2:
            return self.ans
        elif len_word1 > len_word2:
            self.ans += word1[len_word2:]
        else:
            self.ans += word2[len_word1:]

        return self.ans


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) == 1:
            return word1 + word2
        
        i = 0
        # w1: abcd
        # w2: 123
        output = ''
        for char in word1: #abcd
            output += char # a1b, a1b2cd
            if i < len(word2): # 0, 0 < 3; 1, 1 < 3, 2 < 3
                output += word2[i] # a1, a1b2, a1b2c3
                i += 1 # i = 1, i = 2, i + 3
        
        if i <= len(word2):
            output += word2[i:]
        
        return output


        input:
        # w1: abcd
        # w2: 123
                                    
        initial,        |   value |  loop 1 | loop 2 | loop 3
        i, 0
        output, ''
        loop: 'abcd'
            char, a 
            output, 'a', 'b'
            i < len(word)?, yes
                output, 'a1'
                i, 1



return s[::-1]


       head, tail = 0, len(s)-1
       while head < tail:
           prev_tail_val = s[tail]
           s[tail] = s[head]
           s[head] = prev_tail_val
           head += 1
           tail -= 1


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        if len(s) == 1:
            return s

        left = 0
        right = len(s) - 1
        while left <= right:
            temp = s[right]
            # could do temp_left, temp_right
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left+(right-left)//2
            output = guess(mid)
            if output != 1:
                right = mid
            else:
                left = mid+1

        return left
