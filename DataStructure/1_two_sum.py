class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = dict()
        pair = []
        i = 0
        foundPair = False

        while i < len(nums):
            hashTable[nums[i]] = i
            i += 1


        i = 0

        while i < len(nums) and not foundPair:
            compliment = target - nums[i]

            if compliment in hashTable:
                if i != hashTable[compliment]:
                    pair.append((i))
                    pair.append(hashTable[compliment])
                    foundPair = True
            i += 1
        return pair
      
 #https://medium.com/swlh/understanding-leetcode-the-two-sum-problem-6428ed5cb18d
