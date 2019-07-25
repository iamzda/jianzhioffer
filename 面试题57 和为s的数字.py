'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        left, right = 0, len(array) - 1
        while left<=right:
            temp = array[left] + array[right]
            if temp == tsum:
                return [array[left],array[right]]
            elif temp < tsum:
                left += 1
            else:
                right -= 1
        return []
