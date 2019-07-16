
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n=len(array)
        flag='false'
        for i in range(n):
            if target in array[i]:
                flag='true';
                break
        return flag
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(raw_input()))
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break
