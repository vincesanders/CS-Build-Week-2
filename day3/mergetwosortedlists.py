# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # check edge cases
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        # create a new linked list
        head = ListNode()
        current_new = head
        current1 = l1
        current2 = l2
        
        # move through the other linked lists
        looping = True
        while looping:
            if current1 is None and current2 is None:
                looping = False
                break

            # add the node with the lowest value to the new linked list
            if current2 is None or (current1 and current1.val <= current2.val):
                current_new.next = current1
                current_new = current_new.next
                # progress to the next node of that list
                current1 = current1.next
            else:
                current_new.next = current2
                current_new = current_new.next
                # progress to the next node of that list
                current2 = current2.next

        return head.next