https://leetcode.com/problems/count-and-say/description/


2**n *n
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        last_encoded_str = self.countAndSay(n-1) #'1'
        rle_str = ''
        count, val = 0, None
        for i in last_encoded_str:
               if val == None:
                    val = i
                    count = 1
                elif val == i:
                    count += 1
                else:
                    rle_str += str(count)+val
                    val = i
                    count = 1
        # '1' => '11'
        rle_str += str(count) + val
        return rle_str
