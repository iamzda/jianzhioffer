'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0 :
            return 0
        uglylist = [1]
        ugly2 , ugly3 , ugly5 = 0 , 0 , 0
        for i in range(index -1):
            minugly = min(uglylist[ugly2]*2,uglylist[ugly3]*3,uglylist[ugly5]*5)
            uglylist.append(minugly)
            if minugly % 2 ==0:
                ugly2+=1
            if minugly % 3 ==0:
                ugly3+=1
            if minugly % 5 ==0:
                ugly5+=1
        return uglylist[-1]
