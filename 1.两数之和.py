#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = len(nums)
        dict = {}
        for index in range(count):
            dict[nums[index]] = index
        for si in range(count):
            a = nums[si]
            b = target - a
            ei = dict.get(b)
            # 注意两个下标不能重复
            if ei != None and ei != si:
                return [si, ei]
        return []

            

# @lc code=end

