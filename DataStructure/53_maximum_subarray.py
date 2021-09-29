#### best solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         
        final_max_sum = nums[0]
        current_max_sum = nums[0]
        for i in range(1, len(nums)):
            current_max_sum = max(nums[i], current_max_sum + nums[i])
            final_max_sum = max(final_max_sum, current_max_sum)
        return final_max_sum

####  Kadane’s Algorithm

def maxSubArraySum(a, size):
    max_so_far = a[0]
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far
#

# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", maxSubArraySum(a, len(a)))

######## first test
def max_sub_array(a):
    max_sum = a[0]
    current_value = 0

    for i in range(0, len(a)):
        current_value = current_value + a[i]
        if current_value < 0:
            current_value = 0
        elif max_sum<current_value:
            max_sum = current_value

    return max_sum


print(max_sub_array(a))

#### second test
def test(a, size):

    max_value = a[0]
    current = 0
    for i in range(0, size):
        current = current + a[i]
        if current < 0:
            current = 0
        elif max_value < current:
            max_value = current

    return max_value

print(test(a, len(a)))



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        current_value = 0
        for i in range(0, len(nums)):
            current_value += nums[i]
            if current_value < 0:
                current_value = 0
            elif current_value > max_sum:
                max_sum = current_value
        return max_sum
