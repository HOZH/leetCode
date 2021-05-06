#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#

# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        res = []
        
        while label != 1:
            res.append(label)
            label = int('1' + "".join(map(lambda x: '1' if x ==
                                          '0' else '0', format(label, 'b')[1:-1])), 2)
        res.append(1)

        return reversed(res)
# @lc code=end

