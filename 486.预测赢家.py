#
# @lc app=leetcode.cn id=486 lang=python
#
# [486] 预测赢家
#

# @lc code=start
class Solution(object):

    # 递归实现
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def total(s, e, turn):
            if s == e:
                return nums[s] * turn
            ss = nums[s] * turn + total(s + 1, e, -turn)
            se = nums[e] * turn + total(s, e - 1, -turn)
            return max(ss * turn, se * turn) * turn
        return total(0, len(nums) - 1, 1) >= 0
        
# @lc code=end

