'''

'''
class Solution:
    def longestSubstringWithoutDuplication(self, s1):
        curLength, maxLength = 0, 0#curLength相当于书上的f(i)
        position = [-1] * 26  # 这里26表示26个字母，这个list用于保存上一个重复字符的位置
        for i in range(len(s1)):
            prevIndex = position[ord(s1[i]) - ord('a')]  # python无字符串相减，所以用ord将字符转换为ascii码
            if prevIndex < 0 or i - prevIndex > curLength:
                # 后半个判断条件是：当第i位的字符和重复的字符的位置相差大于curLength时，不变
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength
                # 当第i位的字符和重复的字符的位置相差小于curLength时，让curLength=d
                curLength = i - prevIndex # 2个相同字符的距离d
            position[ord(s1[i]) - ord('a')] = i # 保存当先字符的下标
        if curLength > maxLength:
            maxLength = curLength
        return maxLength
