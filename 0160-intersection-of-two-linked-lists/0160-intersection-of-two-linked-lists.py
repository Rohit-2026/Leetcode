class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node: ListNode) -> int:
            cnt=0
            while node:
                cnt+=1
                node=node.next
            return cnt
        lenA,lenB=length(headA),length(headB)
        curA,curB=headA,headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                curA=curA.next
        else:
            for j in range(lenB-lenA):
                curB=curB.next
        while curA is not curB:
            curA=curA.next
            curB=curB.next
        return curA
