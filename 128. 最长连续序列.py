"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：
输入：nums = [1,0,1,2]
输出：3

提示：

- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109
"""

"""
Attempt 1: Sep 5, 2025. `maxlen` 的初始情况写成 1 了。解法没有标答好。
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        numdict = {}
        for num in nums:
            if num in numdict:
                continue
            lower = numdict.get(num - 1, 0)
            upper = numdict.get(num + 1, 0)
            length = 1 + lower + upper
            numdict[num] = length
            if lower:
                numdict[num - lower] = length
            if upper:
                numdict[num + upper] = length
            if length > maxlen:
                maxlen = length
        return maxlen
    
sol = Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(sol.longestConsecutive([1,0,1,2]))