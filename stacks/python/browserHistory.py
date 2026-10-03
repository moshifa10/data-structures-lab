from stack import Stack

class BrowserHistory:

    def __init__(self, back_stack: Stack = Stack([]), forward_stack: Stack = Stack([])):
        self.back_stack = back_stack
        self.forward_stack = forward_stack

        self.default = "Home"
        self.current_page = "Home"


    def visit(self, page):
        self.back_stack.push(self.current_page)
        self.current_page = page
        while not self.forward_stack.is_empty():
            self.forward_stack.pop()

    def back(self):
        if self.back_stack.is_empty():
            return

        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()

    def forward(self):
        if self.forward_stack.is_empty():
            return
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()

    def current(self):
        return self.current_page

if __name__ == "__main__":
    backward_stack = Stack([])
    forward_stack = Stack([])
    history = BrowserHistory(backward_stack, forward_stack)

    # print(history.current())

    # history.forward()
    # print(history.current())

    # history.visit("About")
    # print(history.current())

    # print()

    
    # history.forward()
    # print(history.current())
    # print(backward_stack)
    # print(forward_stack)


    # print()

    # history.back()
    # print(history.current())
    # print(backward_stack)
    # print(forward_stack)

    # print()
    # print("Visit Contact page")

    # history.visit("Contact_page")
    # print(history.current())
    # print(backward_stack)
    # print(forward_stack)

    print(history.current())


    print()
    print("Visit About\n")

    history.visit("About")
    print(history.current())
    print(backward_stack)
    print(forward_stack)

    print()
    print("Visit Contact\n")

    history.visit("Contact")
    print(history.current())
    print(backward_stack)
    print(forward_stack)

    print()
    print("Back\n")

    history.back()
    print(f"Current page: {history.current()}")
    print(f"Back_stack : {backward_stack}")
    print(f"Forward Stack : {forward_stack}")


    print()
    print("Back\n")

    history.back()
    print(f"Current page: {history.current()}")
    print(f"Back_stack : {backward_stack}")
    print(f"Forward Stack : {forward_stack}")

    print()
    print("Forward\n")

    history.forward()
    print(f"Current page: {history.current()}")
    print(f"Back_stack : {backward_stack}")
    print(f"Forward Stack : {forward_stack}")

    print()
    print("Visit Help")

    history.visit("Help")
    print(f"Current page: {history.current()}")
    print(f"Back_stack : {backward_stack}")
    print(f"Forward Stack : {forward_stack}")

    print()
    print("Forward")

    history.forward()
    print(f"Current page: {history.current()}")
    print(f"Back_stack : {backward_stack}")
    print(f"Forward Stack : {forward_stack}")
    




