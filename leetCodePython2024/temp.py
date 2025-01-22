

from collections import defaultdict
[0, 1, 0, 3, 12]
[3, 1, 12, 0, 0] # output
[1, 3, 12, 0, 0] # expected

[4,0,6,0,2,1]
[4,6,2,1,0,0]

# ,  , i, j
# ,  , 2, 0
# break: [4, 6, 2, 0, 1]. i = 2, j = 3
# increment i = 3
# [4, 6, 2, 0, 1]; i is 0, 
# start j at i
[4, 6, 0, 2, 1]  # i = 0 -> 4, i = 1 -> 6, i = 2 -> 0.
                # j 
[4, 6, 2, 1, 0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         for j in range(i+1,len(nums)):
        #             if nums[j]!=0:
        #                 nums[i]=nums[j]
        #                 nums[j] = 0
        #                 break
        zero_indexes = []
        other_indexes = []
        for i in range(len(nums)):
            current = nums[i]
            if current == 0:
                zero_indexes.append(i)
            else:
                other_indexes.append(i)
        for j in other_indexes[::-1]:
            if len(zero_indexes):
                current_index = zero_indexes.pop()
                nums[current_index] = nums[j]
                nums[j] = 0

            else:
                break


def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words_in_list_1 = set(list1)
        bag = defaultdict(int)
        for i in range(len(list2)):
            current = list2[i]
            if current in words_in_list_1:
                bag[current] = i
        for i in range(len(list1)):
            current = list1[i]
            if current in bag:
                bag[current] += i

        min_index_sum = min(bag.values())
        ans = []
        for key, val in bag.items():
            if val == min_index_sum:
                ans.append(key)

        return ans


 def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        word_dict = {}
        common_dict = {}
        output = []
        min_index_seen = 2000

        i = 0
        while i < len(list1):
            word = list1[i]
            word_dict[word] = i
            i += 1

        j = 0
        while j < len(list2):
            word = list2[j]
            if word in word_dict:
                total_index = word_dict[word] + j

                common_dict[word] = total_index
                min_index_seen = min(min_index_seen, total_index)
            j += 1
        
        for k,v in common_dict.iteritems():
            if v == min_index_seen:
                output.append(k)

        return output

from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        # dict_items([(1, 3), (2, 2), (3, 1)])
        seen = set()
        for val in counter.values():
            if val not in seen:
                seen.add(val)
            else:
                return False
        return True

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) == 1:
            return True
        
        num_dict = {}
        print '123'

        '{0.b}'.format(8)
        for i in xrange(len(arr)):
        for i,char in enumerate(arr):
        for i in arr: ['a', 'b', 'c', 'd']
        
        i = 0
        while i < len(arr):
            val = arr[i]
            # num_dict[val]+=1 # {key: 0} defaultdict
            if val not in num_dict:
                num_dict[val] = 1
            else:
                num_dict[val] += 1
            i += 1
        
        seen = set()
        for v in num_dict.values():
            if v not in seen:
                seen.add(v)
            else:
                return False
        
        return True