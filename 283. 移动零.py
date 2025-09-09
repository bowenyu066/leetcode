"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]

提示:

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

进阶：你能尽量减少完成的操作次数吗？
"""

"""
Attempt 1: Sep 8, 2025. 我们和官方做法都是双指针，但是有所不同。
官方做法是双指针交换，有快排思想蕴含在其中，可以慢慢品味。
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0; right = 0
        L = len(nums)
        while right < L:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
            right += 1
        while left < L:
            nums[left] = 0
            left += 1
            
sol = Solution()
nums = [0,1,0,3,12]; sol.moveZeroes(nums); print(nums)
nums = [0]; sol.moveZeroes(nums); print(nums)