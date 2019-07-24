'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global re
        re = []
        self.mid(pRoot)
        if  k<=0 or len(re)<k:
            return None
        else:
            return re[k-1]
    def mid(self, root):
        if not root:
            return None
        self.mid(root.left)
        re.append(root)
        self.mid(root.right)
