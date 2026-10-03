from stack import Stack


'''

    Build a minimum stack — Medium–Hard
    Create a MinStack with push(number), pop(), peek() and get_min().
    Requirement: get_min() must return the smallest number in O(1) time—without scanning or sorting the stack. Empty pop(), peek() and get_min() calls should return None.
    Check duplicate minimum values: push 5, 2, 2. After popping one 2, the minimum should still be 2. After popping the second, it should become 5. Also test negative numbers.

'''


class MinStack:
    def __init__(self):
        self.main_stack = Stack([])
        self.min_stack = Stack([])

    def push(self, number):
        self.main_stack.push(number)

        # Store new minimums, including duplicates.
        if self.min_stack.is_empty() or number <= self.min_stack.peek():
            self.min_stack.push(number)

    def pop(self):
        if self.main_stack.is_empty():
            return None

        number = self.main_stack.pop()

        if number == self.min_stack.peek():
            self.min_stack.pop()

        return number

    def peek(self):
        if self.main_stack.is_empty():
            return None

        return self.main_stack.peek()

    def get_min(self):
        if self.min_stack.is_empty():
            return None

        return self.min_stack.peek()