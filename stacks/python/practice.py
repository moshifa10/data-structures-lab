

# Stacks - Books

class Stack:

    def __init__(self, **args):
        self.stack_: list = None
        if args:
            self.stack_ = args["stack"]

    def push(self, book):
        if not isinstance(self.stack_, list):
            self.stack_ = []
        self.stack_.append(book)
        return self.stack_
       
    def pop(self):
        if not isinstance(self.stack_, list):
            return
        if self.is_empty():
            return None
        return self.stack_.pop()

    def peek(self):
        if not isinstance(self.stack_, list):
            return
        if self.is_empty():
            return
        return self.stack_[-1]

    def is_empty(self):
        if not isinstance(self.stack_, list):
            self.stack_ = []
        return not len(self.stack_) > 0

    def size(self):
        return len(self.stack_)


my_list = ["Njabs", "Busa", "Stha"]
my_stack = Stack(stack=my_list)

print(my_stack.pop())
print(my_stack.size())
print(my_stack.peek())

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.size())

