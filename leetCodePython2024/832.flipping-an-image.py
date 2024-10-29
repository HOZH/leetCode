#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]

        for i in range(len(image)):
            image[i] = list(map(lambda x: (1 if x == 0 else 0), image[i]))

        return image

# @lc code=end
