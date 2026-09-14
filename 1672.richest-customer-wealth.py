#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self,accounts):
        max_c=0
        for i in accounts:
            wealth=sum(i)

            if max_c <= wealth:
                max_c=wealth
        
        return max_c

# @lc code=end

