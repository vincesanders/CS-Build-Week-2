# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        
        p = headA
        
        # Add all list A nodes to a set
        while p is not None:
            seen.add(p)
            p = p.next
            
        # Run through list B looking for seen nodes
        p = headB
        
        while p is not None:
            if p in seen:
                return p
            
            p = p.next
            
        # If we got here, we didn't find an intersection
        return None