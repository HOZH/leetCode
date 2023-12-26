#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.wordList = set(wordList)

        len_word = len(beginWord)

        def valid_next_word(w1, w2):
            flag = True
            for i in range(len_word):
                if w1[i] != w2[i]:
                    if not flag:
                        return False
                    flag = False

            return True

        if endWord not in wordList:
            return 0

        def valid_next_words(word):
            ans = set()
            for i in self.wordList:
                if valid_next_word(i, word):
                    ans.add(i)
            for i in ans:
                self.wordList.remove(i)
            return ans

        steps = 1
        stack = set([beginWord])
        visited = set()
        max_len = len(wordList)+1
        while len(stack) > 0:
            if steps > max_len:
                return 0
            next_layer = set()
            while len(stack):
                current = stack.pop()
                if current in visited:
                    continue
                if current == endWord:
                    return steps
                visited.add(current)
                for i in valid_next_words(current):
                    if i not in visited:
                        next_layer.add(i)
            stack = next_layer
            steps += 1

        return 0


# @lc code=end
