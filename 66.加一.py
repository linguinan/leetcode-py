#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    # 递进及溢出处理
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9:
                digits[i] = 0
                digits[i - 1] += 1
        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


# @lc code=end
