# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Create a pointer for the previous node and the head node of the new linked list
        prev = None
        head = None
        
        # Create pointer for the current nodes of the passed in linked lists
        # as we traverse them
        currentL1 = l1
        currentL2 = l2
        
        # create a variable to store a carry value if our values add up to more than 10
        carry = 0
        
        # traverse l1 and l2 at the same time
        while currentL1 is not None or currentL2 is not None:
            
            # add their values to get value of new linked list
            # check for edge cases where one linked list is longer than another.
            newValue = 0
            if currentL1 is None:
                newValue = currentL2.val + carry
            elif currentL2 is None:
                newValue = currentL1.val + carry
            else:
                newValue = (currentL1.val + currentL2.val) + carry
            
            # reinitialize carry
            carry = 0
            
            # if the new value is above 10, we need to carry the 1
            # and get the number modulus 10
            if newValue >= 10:
                carry = 1
                newValue = newValue % 10
                
            # Create a new node for our new linked list
            newNode = ListNode(newValue)
            
            # if we have a previous node, set it's next attribute to the new node
            if prev is not None:
                prev.next = newNode
                
            # if we don't have a previous node, this is the first node,
            # set it to the head of the new linked list
            else:
                head = newNode
                
            # Set the previous node to the new node
            # and set currentL1 and currentL2 to the next node
            # and continue with traversal.
            prev = newNode
            if currentL1 is not None:
                currentL1 = currentL1.next
            if currentL2 is not None:
                currentL2 = currentL2.next
            
        # check for carry after full traversal of the list
        if carry > 0:
            prev.next = ListNode(carry)
            
        # return the head node of our new linked list
        return head