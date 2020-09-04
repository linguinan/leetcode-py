#
# @lc app=leetcode.cn id=7 lang=python
#
# [7] 整数反转
#

# @lc code=start
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        numStr = str(x)
        retStr = ""
        count = len(numStr)
        if count == 0:
            return 0
        # 符合判断
        si = -1
        if numStr[0] == "-":
            si = 0
            retStr += numStr[0]
        # 排除最后的0
        if count - si > 2:
            for i in range(count - 1, si, -1):
                if numStr[i] == "0":
                    count -= 1
                break
        # 翻转
        for i in range(count - 1, si, -1):
            retStr += numStr[i]
        # 检查溢出
        max = 2**31 - 1
        min = -2**31
        ret = int(retStr)
        if ret > max or ret < min:
            ret = 0
        return ret

# @lc code=end

