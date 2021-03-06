#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        count = 0
        temp = head
        while (temp.next != None):
            count+=1
            temp = temp.next
        
        sum = 0 
        while (head != None):
            sum += head.val * pow(2, count) 
            count -= 1
            head = head.next
        
            
        return sum
