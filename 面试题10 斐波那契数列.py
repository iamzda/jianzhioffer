#斐波那契数列
class Solution:
    def Fibonacci(self, n):
        # write code hereb
        if n ==0:
            return 0
        elif n ==1:
            return 1
        else:
            a = []
            a.append(0)
            a.append(1)
            for i in range(2,n+1):
                s = a[i-1] +a[i-2]
                a.append(s)
            return a[n]
