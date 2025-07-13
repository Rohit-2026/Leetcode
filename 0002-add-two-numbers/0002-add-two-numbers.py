# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t=""
        while l1:
            t+=str(l1.val)
            l1=l1.next
        t1=""
        while l2:
            t1+=str(l2.val)
            l2=l2.next
        total=int(t[::-1])+int(t1[::-1])
        dummy=ListNode(0)
        cur=dummy
        for d in str(total)[::-1]:
            cur.next=ListNode(int(d))
            cur=cur.next
        return dummy.next

            

        