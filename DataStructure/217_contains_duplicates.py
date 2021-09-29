####
#OOP solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
                return True
        return False
##
s = input()
my_list = list(map(int, s.split()))

if len(my_list) == len(set(my_list)):
    print('false')
else: 
    print('true')
