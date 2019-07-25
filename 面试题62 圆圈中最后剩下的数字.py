'''

'''
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n or not m:
            return -1
        i = 0
        nums = range(n)
        while len(nums)>1:
            i = (m+i-1)%len(nums)
            nums.pop(i)
        return nums[0]
