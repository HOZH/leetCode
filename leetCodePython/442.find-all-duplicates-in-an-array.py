#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        #o(n) space(n)
        #check back later on https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/353940/Simple-Java-O(n)-solution-using-swap-for-slow-learners-like-myself
        counter= collections.Counter(nums)

        lis=list()


        for i in counter:

            if counter[i]==2:

                lis.append(i)

        lis.sort()
        return lis



        

