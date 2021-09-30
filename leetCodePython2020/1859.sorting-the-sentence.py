#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:

        placeholder = s.split(' ')
        temp_list = []
        for seq in placeholder:
            index = 0
            for j in range(len(seq)):
                if ord(seq[j]) in range(48, 58):
                    break
                index += 1
            temp_list.append((seq[:index], int(seq[index:])))

        temp_list.sort(key=lambda x: x[1])

        return ' '.join(list(map(lambda x: x[0], temp_list)))


# @lc code=end
