from stack import Stack

'''

    Convert a number to binary — Easy–Medium
    Write to_binary(number) for non-negative integers. Use a stack to arrange the binary digits in the correct order.
    Examples:
    - 13 → "1101"
    - 2 → "10"
    - 0 → "0"
    Constraint: Don’t use bin() or binary formatting.

'''


# Example 
    # 
    # 1101
            

# 56 -> 111000 

def from_binary(number: str) -> int:
    counter = 0
    sum_ = 0


    number_list = list(map(int,list(str(number))))
    stack = Stack(number_list)

    while not stack.is_empty():
        popped = stack.pop()
        sum_ += popped * pow(2, counter)
        counter += 1

    return sum_


def to_binary(number: int) -> str:
    if number == 0:
        return "0"
    expo = 0
    powers = []
    binary_reversed = []

    while pow(2, expo) <= number:
        powers.append(pow(2, expo))
        expo += 1

    for i in range(len(powers)-1, -1, -1):
        div, remainder = divmod(number, powers[i])
        if div > 0:
            number = remainder
            binary_reversed.append(powers[i])
            continue
        binary_reversed.append(0)

    binary_code = [1 if binary_reversed[i]>0 else 0  for i in range(len(binary_reversed))]

    return "".join(list(map(str,binary_code)))


# Another way
def to_binary(number: int) -> str:
    if number == 0:
        return "0"

    powers = Stack([])
    power = 1

    # Push powers in ascending order.
    while power <= number:
        powers.push(power)
        power *= 2

    binary_digits = []

    # Pop powers in descending order.
    while not powers.is_empty():
        power = powers.pop()
        digit, number = divmod(number, power)
        binary_digits.append(str(digit))

    return "".join(binary_digits)


if __name__ == "__main__":
    # print(from_binary("1101"))
    # print(from_binary("111000"))

    print(to_binary(13)) # -> 1101
    print(to_binary(2))
    print(to_binary(0))
    print(to_binary(3))
    print(to_binary(1))
    print(to_binary(9))
    print(to_binary(25))
    print(to_binary(42))
    print(to_binary(100))
    print(to_binary(100))


        



