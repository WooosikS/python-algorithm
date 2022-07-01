# # 브루트 포스
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#                 else:
#                     continue

# nums = [2, 7, 11, 15]
# target = 9
# print(Solution.twoSum(0, nums, target))


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            print(i, num)
            nums_map[num] = i
            print(nums_map[num])
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [ i, nums_map[target - num] ]
         
nums = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(0, nums, target))