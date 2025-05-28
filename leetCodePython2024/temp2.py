operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    # Avoid division by zero
    '/': lambda a, b: a / b if b != 0 else float('inf'),
    '^': lambda a, b: a ** b  # Exponentiation operator
}


a= operators['+'](1, 2)
print(a)
b = lambda a, b: a + b
print(b(2,3))

input = [8,9,9]
8^9 = 1 
0 = 0000
8 = 1000
9 = 1001
result xor of 8 and 9 = 0001
result = 1
If we take 'exclusive or'  of zero and some bit, it will return that bit



input = [4,1,2,1,2]

          p1, 
0 = 0
1 = 1
2 = 10
3 = 11


nums = [2, 2, 1]


class Solution(object):
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
    

# 1
a = 0 

a = a ^ 2
# 00
# 10
# 10
# 2
a = 2
a = 2 ^ 2 

# 3 
a = 0
a = 0 ^ 1
a =1 


[4, 1, 2, 1, 2]
# 1 
a = 0
a = 0 ^ 4 # -> 4
# 2
a = 4
a = 4 ^1 # -> 5
# 3 
a = 5
a = 5 ^ 2 # -> 7
# 4
a = 7
a = 7 ^ 1 # -> 6
# 5 
a =6 
a = 6 ^ 2 # -> 4

# 6
a = 4

score =
[10,3,8,9,4]

 heaps [3, 4, 8, 9, 10]

# key is the index from score
#  {
#     0: 10
#     1: 3
#     2: 8
#     3: 9
#     4: 4
#  }

 {
    10: 0
    3: 1
    8: 2

 }


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        bag = {}
        for index, value in enumerate(sorted_scores):
            if index == 0:
                bag[value] = "Gold Medal"
            elif index == 1:
                bag[value] = "Silver Medal"
            elif index == 2:
                bag[value] = "Bronze Medal"
            else:
                bag[value] = str(index + 1)

        ans = []
        for i in score:
            ans.append(bag[i])
        return ans

        return list(map(lambda x: bag[x], score))




# input: "abcdefg", k2
# ab
# start_counter - i
#counter 0, 1, 2 == k

 def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]

        output = ''
        start_counter = 0
        should_skip = False

        counter = 0
        for i,char in enumerate(s):
            if counter != k: # k=2 i % k, 
                counter += 1
            else:
                # if should_skip == True:
                #     counter += 1
                #     continue
                piece = s[start_counter:i] # s[0:2], 'ab' cd
                rev_piece = piece[::-1] # s[0:2:-1], 'ba
                output = output + rev_piece # '' -> ba, bacd
                if should_skip == False:
                    output = output + rev_piece
                    should_skip = True
                else:
                    output = output + piece
                    should_skip = False
                start_counter = i
                counter = 0
        
        index_where_stopped_process = len(s) // k * k
        for _ in range(index_where_stopped_process, len(s)):
            pass

        # abcdefg -> ab, cd, ef, g -> ba, cd, ef, g
        return output + s[start_counter:counter]

s[0:2][::-1]



