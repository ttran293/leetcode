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
          
        
#Solution2: x2 performance
        node1 = head
        node2 = head
        count = 1
        while not node1.next == None:
            if count > n:
                node2 = node2.next
            node1 = node1.next
            count += 1
        
        if count == n:
            return head.next
        
        if not node2.next.next == None:
            node2.next = node2.next.next
        else:
            node2.next = None
        return head
