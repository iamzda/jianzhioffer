'''

'''
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # 如果扑克牌为空，返回假
        if not numbers or len(numbers) < 5:
            return False
        # write code here
        numbers.sort()
        # 输出0的个数
        zero_num = 0
        for i in range(0, len(numbers)):
            if numbers[i] != 0:
                zero_num = i
                break
        # 输出gap的个数
        start = zero_num
        next = zero_num + 1
        end = len(numbers)
        gap_num = 0
        while next < end:
            # 如果出现对子的情况，一定不可能成为顺子
            if numbers[next] == numbers[start]:
                return False
            gap_num += numbers[next] - (numbers[start] + 1)
            start = next
            next += 1
        # 判断能够成为顺子
        if zero_num >= gap_num:
            return True
        return False
