'''

'''
class Solution:
    def MaxDiff(self,numbers):
        if not numbers or len(numbers) < 2:
            return 0
        minVal = numbers[0]
        maxDiff = numbers[1] - minVal
        for i in range(2,len(numbers)):
            # 更新最小值
            if numbers[i-1] < minVal:
                minVal = numbers[i-1]

            # 计算差值
            curDiff = numbers[i] - minVal
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff
