#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        if not len(s):
            return 0
        liz = s.split(' ')
        return len(list(filter(lambda x: x !='',liz)))
        
# @lc code=end

def countSegments(self, s: str) -> int:
        unfiltered_segments = s.split(' ')
        return len(list(filter(lambda seg: seg != '', unfiltered_segments)))




def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        special_chars = [
            '"',
            "!",
            "@",
            "#",
            "$",
            "%",
            "^",
            "&",
            "*",
            "(",
            ")",
            "_",
            "+",
            "-",
            "=",
            "'",
            ",",
            ".",
            ":",
        ]

        for char in s:
            prev_char = None
            if prev_char != None and prev_char not in special_chars:
                prev_char = char
                continue
            # test for character continuguous
            if char not in special_chars and prev_char not in special_chars:
                prev_char = char
                continue
            # param = '    ' -> 0
            # temp = param.split(' ') # temp = ['','','','']
            # param = '        abc        dfe          '
            # param = 'abc dfe'
            

            if char in special_chars and prev_char not in special_chars:
                prev_char = char
                continue
            
            if char in special_chars and prev_char in special_chars:
                output += 1
        return output