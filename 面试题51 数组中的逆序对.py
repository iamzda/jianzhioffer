'''
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''
import sys
sys.setrecursionlimit(1000000)
class Solution:
    def InversePairs(self, data):
        if not data :
            return 0
        Copy = [i for i in data]
        count = self.InversePairsCore(data, Copy, 0, len(data) - 1)
        del Copy
        return count % 1000000007

    def InversePairsCore(self,data,Copy,start,end):
        if start == end:
            Copy[start] == data[start]
            return 0

        mid = int((start + end) / 2)

        left = self.InversePairsCore(Copy, data, start, mid)
        right = self.InversePairsCore(Copy, data, mid + 1, end)

        # 下面相当于merge
        # i初始化为前半段最后一个数字的下标，j初始化为后半段最后一个数字的下标
        i, j = mid, end
        indexCopy = end
        count = 0
        while i >= start and j >= mid + 1:
            if data[i]>data[j]:
                Copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - mid
            else:
                Copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        # 进行到这里，说明知道有一个数组已经到头了，或者是i或者是j
        while i >= start:
            Copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        while j >= mid + 1:
            Copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left + right + count
