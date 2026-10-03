from stack import Stack

'''
    Check balanced brackets — Medium
    Write balanced_brackets(text). The input contains only (), [] and {}. Return whether every opening bracket has a matching closing bracket in the correct order.
    Examples:
    - "([]{})" → True
    - "([)]" → False
    - "())" → False
    - "" → True
    Constraint: Use a stack.

'''



def balance_brackets(text: str) -> bool:

    combinations = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack = Stack([])

    for idx, b in enumerate(text):
        if b in combinations:
            stack.push(b)
        elif not stack.is_empty() and b == combinations[stack.peek()]:
            stack.pop()
        else:
            return False

    return False if not stack.is_empty() else True


if __name__ == "__main__":

    print(balance_brackets("([]{})"))
    print(balance_brackets("([)]"))
    print(balance_brackets("())"))
    print(balance_brackets(""))
    print(balance_brackets("}}"))

    print()
    print(balance_brackets("((()))"))
    print(balance_brackets("()[{}]"))
    print(balance_brackets("{[()]}"))
    print(balance_brackets("[[[]]"))
    print(balance_brackets("(()))("))


    print()
    print(balance_brackets("(])"))
    print(balance_brackets("[)]"))
    print(balance_brackets("{)}"))
    print(balance_brackets("([}])"))
    print(balance_brackets("({]})"))

