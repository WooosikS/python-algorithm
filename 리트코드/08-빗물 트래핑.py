# Stack 풀이

# class Solution:
#     def trap(self, height: list[int]) -> int:
#         stack = []
#         volume = 0

#         for i in range(len(height)):
#             while stack and height[i] > height[stack[-1]]:
#                 top = stack.pop()

#                 if not len(stack):
#                     break

#                 distance = i - stack[-1] -1
#                 waters = min(height[i], height[stack[-1]]) - height[top]

#                 volume += distance * waters

#             stack.append(i)
#         return volume

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(Solution.trap(0, height))


# 투 포인터 풀이

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        volume = 0
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if height[left] <= height[right]:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution.trap(0, height))