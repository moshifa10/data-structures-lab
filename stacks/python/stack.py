

# Stacks - Books

class Stack:

    def __init__(self, stack: list):
        self.stack_: list = stack

    def push(self, book):
        self.stack_.append(book)
        return self.stack_
       
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_.pop()

    def peek(self):
        if self.is_empty():
            return
        return self.stack_[-1]

    def is_empty(self):
        return len(self.stack_) == 0

    def size(self):
        return len(self.stack_)



if __name__ == "__main__":
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

