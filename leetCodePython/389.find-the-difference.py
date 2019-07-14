#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        my_dict = dict()

        for i in t:
            if my_dict.get(i) ==None:
                my_dict[i]=1

            else:
                my_dict[i]=my_dict[i]+1


        for i in s:
            
            if my_dict[i] != 1:
                my_dict[i]= my_dict[i]-1
            else:
                 del my_dict[i]


        return list(my_dict.keys())[0]

        

