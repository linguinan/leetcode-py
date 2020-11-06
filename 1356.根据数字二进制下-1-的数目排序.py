#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:

    def hammingWeight(self, num):
        """
        计算数字二进制中1的数目
        """
        res = 0
        while num > 0:
            if num & 1:
                res += 1
            num = num >> 1
        return res

    def sortByBits(self, arr: List[int]) -> List[int]:
        count = len(arr)
        arr = sorted(arr)
        print(arr)
        tmp = []
        for num in arr:
            tmp.append(self.hammingWeight(num))
        print(tmp)
        for i in range(count - 1):
            flag = False
            # 每次循环把最大的放在最后
            for j in range(count - i - 1):
                # print(i, j)
                if tmp[j] > tmp[j + 1]:
                    tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:
                break
        return arr

# @lc code=end
