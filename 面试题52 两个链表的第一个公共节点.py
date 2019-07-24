'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        stack1 = []
        atack2 = []
        node1 = pHead1
        node2 = pHead2
        while node1:
            stack1.append(node1.val)
            node1 = node1.next
        while node2:
            if node2.val in stack1:
                return node2
            else:
                node2 = node2.next
                
