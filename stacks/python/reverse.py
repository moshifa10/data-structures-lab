from stack import Stack


# Activity 1

'''

    Reverse a string — Easy
    Write reverse_text(text) using a stack. Push the characters, then use popping to build the reversed string.
    Examples:
    - "stacks" → "skcats"
    - "Java" → "avaJ"
    - "" → ""
    Constraint: Don’t use slicing, reversed() or a built-in reverse method.

'''

def reverse_text(text: str) -> str:

    formatted_text = list(text)
    my_stack = Stack(formatted_text)
    reverse = []

    while not my_stack.is_empty():
        reverse.append(my_stack.pop())
    return "".join(reverse)

if __name__ == "__main__":
    print(reverse_text("Java"))