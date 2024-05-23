
# https://leetcode.com/problems/two-sum/description/



def twoSum(nums, target):

    for pos1, value1 in enumerate(nums):
        for pos2, value2 in enumerate(nums):

            if pos1 != pos2:
                result = value1 + value2

                if result == target:
                    return[pos1, pos2]





print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))