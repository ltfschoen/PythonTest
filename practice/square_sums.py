#
# Comparison of basic Sequential solution versus more advanced Functional solution
#

import sys; assert sys.version_info >= (3,6,0)

def sequentially_calculate_sums_squared(nums):
    total = 0
    for i in range(len(nums)):
        total = (total + nums[i]**2)
    return total

def functionally_calculate_sums_squared(nums):
    return sum(x**2 for x in nums)

nums = [1, 2]
print ( ("Sequentionally calculating sums squared of {} is: {}".format(nums, sequentially_calculate_sums_squared(nums))) )
print ( ("Functionally calculating sums squared of {} is: {}".format(nums, functionally_calculate_sums_squared(nums))) )