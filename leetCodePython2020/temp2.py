class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)
        key_press_pairs = [(key, counter[key]) for key in counter]
        key_press_pairs.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for i in range(len(key_press_pairs)):
            key, press = key_press_pairs[i]
            if i<9:
                ans+=press*1
            elif i<18:
                ans+=press*2
            else:
                ans+=press*3
        return ans


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative, positive = [], []
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                positive.append(i)
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
        return result


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return ans

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp = set()
        for i in nums:
            if i in temp:
                temp.remove(i)
            else:
                temp.add(i)
        return temp
