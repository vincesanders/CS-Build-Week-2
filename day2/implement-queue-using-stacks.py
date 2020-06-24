class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return f'Node: value-{self.value} next-{self.next}'
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        # set this node's next reference to the passed in node
        self.next = new_next

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head
        self.size = 1

    def is_empty(self):
        return self.head == None

    def prepend(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return True
        if self.head.value == None:
            self.head.value = value
            return True
        new_node = Node(value)
        head = self.head
        new_node.next = head
        self.head = new_node
        self.size += 1

    def remove_head(self):
        if self.is_empty():
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.prepend(value)

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.storage = [Stack(), Stack()]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.size += 1
        self.storage[0].push(x)

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.storage[0]) is 0 is len(self.storage[1]):
            return None
        elif len(self.storage[1]) is 0: # if stack 2 is empty
            while len(self.storage[0]) is not 0: # move all but last to stack 2
                self.storage[1].push(self.storage[0].pop())
        return self.storage[1].storage.head.value # return the value of the node at the top of the second stack

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.storage[0]) is 0 and len(self.storage[1]) is 0:
            return None
        elif len(self.storage[1]) is 0: # if stack 2 is empty
            while len(self.storage[0]) is not 1: # move all to stack 2
                self.storage[1].push(self.storage[0].pop())
            value = self.storage[0].pop() # remove the last
        else: # there are items in stack 2
            value = self.storage[1].pop()
        self.size -= 1
        return value

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size is 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
["MyQueue","push","push","peek","pop","empty"]
[[],[1],[2],[],[],[]]
'''

q = MyQueue()
q.push(1)
print(q.storage[0].storage.tail.value)
print(q.pop())
print(q.empty())