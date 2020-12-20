# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #pointer to head
        count = 1
        count2= 1
        temp = head
        while (temp.next is not None):
            count+=1
            temp=temp.next
                
        temp = head
        #if count = 1, delete head return empty list
        if (count == 1):
            head = None
            return head
        #else: count >= 1
        else:
            #if n == 1 delete tail
            if (n==1):
                while(temp.next.next is not None):
                    temp=temp.next
                temp.next = None
                return head
            #else n>1 delete in middle or head
            else:
                if (count2 == (count-n+1)):
                    head = temp.next
                    return head
                else:
                    while(temp.next is not None):
                        if (count2+1 == (count-n+1)):
                            temp.next = temp.next.next
                            return head
                        count2+=1
                        temp= temp.next
            
