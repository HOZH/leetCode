#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            longer_str = str1
            short_str = str2
        else:
            longer_str = str2
            short_str = str1

        current_candiate = short_str
        len_longer = len(longer_str)
        len_shorter = len(short_str)

        while len(current_candiate) > 0:
            # divmod(6,3) = 2,0
            ratio, remainder = divmod(len_longer, len(current_candiate))
            ratio_shorter, remainder_shorter = divmod(
                len_shorter, len(current_candiate))
            if remainder == 0 and remainder_shorter == 0 and current_candiate*ratio == longer_str and current_candiate * ratio_shorter == short_str:
                return current_candiate
            current_candiate = current_candiate[:-1]

        return ''

# @lc code=end


Input: str1 = "AAAAAB", str2 = "AAA"


if len(str2) > len(str1):
    # assign
short_str = str2  # AAA
long_str = str1  # AAAAAB

for loop  # AA
if len(long_str) % len(short_str) == 0:  # implies whole number
    full_str = short_str ** 2
    # loop to compare
else:




class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ''

        short_str = str2
        long_str = str1
        if len(str2) > len(str1):
            short_str = str1
            long_str = str2
        
        candidate = ''
        mult = 1
        print('loop: ', long_str, short_str)

        # ABABAB
        # ABAB
        # output : AB

        i = len(short_str)
        while i >= 0:
            curr_str = short_str[0:i]
            if len(long_str) % len(curr_str) == 0: # 6 , 3
                output = short_str[0:i] # AB
                candidate = short_str[0:i] # ABA
                mult = len(long_str) // len(short_str) # 6 // 3 -> 2
                if candidate * mult == long_str:
                   mutl_ratio_for_short, remainer_for_shorter = divmod(shorter_str, candidate) 
                   # 2, 0 
                   if remainer_for_shorter == 0 and candidate*mutl_ratio_for_short == short_str:
                       return candidate
                       
                
            i -= 1
        long = abab
        short = abbb
        abbb # 1st loop
        abb # 2nd loop
        ab # 3rd loop

        candidate = ab
        ab*2 = abab
        ab*2 != abbb -> here we fail



        print('cand: ', candidate)
        
        candidate *= mult # ABCABC
        # if candidate == long_str:
        #     return output
        # if candidate == long_str
        j = 0
        while j < len(candidate):
            curr_cand = candidate[j]
            if curr_cand != long_str[j]:
                break
            j += 1

        return output