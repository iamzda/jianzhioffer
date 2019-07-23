'''

'''
class Solution:
    def getMaxValue_solution1(self,values):
        if not values:
            return 0
        cols,rows = len(values),len(values[0])
        maxValues = [[0 for i in range(rows)] for i in range(cols)]
        for i in range(cols):
            for j in range(rows):
                left, up = 0, 0
                if i >0:
                    up = maxValues[i-1][j]
                if j >0:
                    left = maxValues[i][j-1]
                maxValues[i][j] = max(up,left) + values[i][j]
        return maxValues[i-1][j-1]
