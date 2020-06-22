class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current = head
        visited = set()
        
        #traverse the linked list
        while current is not None:
            
            # check if we have visited the node before.
            if current in visited:
                return True
            
            # Mark node as visited and move to the next node
            visited.add(current)
            current = current.next
            
        # If we get to this point, no cycles were found.
        return False