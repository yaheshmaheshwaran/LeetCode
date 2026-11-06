#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l=0
        for r in range (len(nums)):
            if nums[r]!=0:
                nums[r],nums[l]=nums[l],nums[r]
                l+=1
        
# @lc code=end

