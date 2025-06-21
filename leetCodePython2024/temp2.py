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


def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        prev_day = ''
        # is_late = False

        for char in s:
            if char == "A":
                absent_count += 1
                # if absent_count >= 2: quick return True
            elif char == "L":
                late_count += 1
                if prev_day == char:
                    late_count += 1
                else:
                    late_count = 0
                if late_count >= 2:
                    # is_late = True 
                    return False
            prev_day = char

        # "PPALLL"
        # P,P,A, 
        # L, late_count = 0, late_count = 1
        # L, L, late_count = 1, late_count = 2, 3
        # L, L, late_count = 2
        # LPLPLPLPL

        # LLLALL
        if absent_count >= 2 or is_late == True:
            return False
        return True




class Solution:
    # LPLPLPLPL

    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_count = 0
        for i in s:
            if i == 'L':
                late_count += 1
                if late_count > 2:
                    return False
            else:
                if i == 'A':
                    absent_count += 1
                late_count = 0

            if absent_count > 1:
                return False


        return True





class Solution:
    global_node = 0

    def start(self, root) -> int:
        self.averageOfSubtree(root)
        return self.global_node # int, -> # 24, 6


    def averageOfSubtree(self, root: TreeNode): -> (?node.val, int)
        if root is None:
            return None, 0

        left, left_total_node = self.averageOfSubtree(root.left)
        right, right_total_node = self.averageOfSubtree(root.right)
        total_nodes = 1

        left_node_val = 0
        right_node_val = 0

        if left is not None:
            total_nodes += left_total_node
            left_node_val = left
        if right is not None:
            total_nodes += right_total_node
            right_node_val = right
        
        avg_val = (root.val + left_node_val + right_node_val) // total_nodes
        # print('curr node val: ', root.val , ' sub nodes and self: ', total_nodes, ' avg: ', avg_val)
        if avg_val == root.val:
            self.global_node += 1
            # print('avg == root: curr global_node: ', self.global_node, ' global node: ', root.val)
        
        total_val = root.val
        if left is not None:
            total_val += left_node_val
        if right is not None:
            total_val += right_node_val
        return total_val, total_nodes


function outerFunction(outerVar) {
    const someFunction = () => {}
  function innerFunction(innerVar) {
    console.log("Outer variable:", outerVar); // Accessing outer variable
    console.log("Inner variable:", innerVar);
  }
  innerFunction();
  return innerFunction;
}

function innerFunction(innerVar) {
    console.log("Outer variable:", outerVar); // Accessing outer variable
    console.log("Inner variable:", innerVar);
  }

function outer( $msg ) {
    function inner( $msg ) {
        echo 'inner: '.$msg.' ';
    }
    echo 'outer: '.$msg.' ';
    inner( $msg );
}


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        consecutive_odd = 0
        for n in arr:
            is_odd = (n % 2) == 1
            if is_odd:
                consecutive_odd += 1
            else:
                consecutive_odd = 0
            
            if consecutive_odd == 3:
                return True
            


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_nums = []
        prev = 0
        for i in arr:
            missing_nums.extend(range(prev + 1, i))
            prev = i
        for i in range(arr[-1]+1, 2002):
            missing_nums.append(i)
        return missing_nums[k-1]

[1].extend([2,3])
[1,2,3]




class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last_num = arr[-1]
        full_list = list(range(1, last_num))

        arr_set = set(arr)

        missing_list = []

        for num in full_list:
            if num not in arr_set:
                missing_list.append(num)

        # arr= [1,2,3,4], k = 2 , missing_list = []
        if len(missing_list) == 0:
            return last_num + k
        # arr = [5,6,7,8], missing_list = [1,2,3,4], full_list = [1,2,3,4,5,6,7,8]
        return missing_list[k - 1]



        addtional_count = k - len(missing_list)
        last_num+addtional_count