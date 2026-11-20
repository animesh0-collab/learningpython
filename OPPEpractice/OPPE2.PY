#2026OPPE set2
#Problem 1 
def reverse_first_half(s: str) -> str:
    """
    Write a function reverse_first_half(s) that returns a new string in which the first half of s is reversed and the second half is left as it is.

    Examples:
    reverse_first_half("abcdef") -> 'cbadef'
    reverse_first_half("python") -> 'typhon'
    """
    s1 = len(s) // 2
    s2 = s[:s1]
    s3 = s2[::-1]
    return s3 + s[s1:]

#Problem 2
def train_ticket(passenger: dict, available_seats: int) -> str:
    """
    passenger is a dictionary with the keys "age" and "has_id" (True or False). Write
    a function train_ticket(passenger, available_seats) that checks these rules in this
    order and returns the answer of the first rule that applies:

    1. If the passenger has no ID, return "ID Required".
    2. If available_seats is 0, return "Waiting List".
    3. If the passenger is 60 years old or older, return "Priority Booking".
    4. Otherwise, return "Ticket Confirmed".

    Examples:
    train_ticket({"age": 65, "has_id": True}, 5) -> 'Priority Booking'
    train_ticket({"age": 30, "has_id": False}, 5) -> 'ID Required'
    """
    if not passenger["has_id"]:
        return "ID Required"
    elif available_seats == 0:
        return "Waiting List"
    elif passenger["age"] >= 60:
        return "Priority Booking"
    else:
        return "Ticket Confirmed"

#Problem 3
def double_if_even_else_square(n: int) -> int:
    """
    Write a function double_if_even_else_square(n) that returns n multiplied by 2 if n is
    even, and the square of n if n is odd.

    Examples:
    double_if_even_else_square(8) -> 16
    double_if_even_else_square(9) -> 81
    """
    if n % 2 == 0:
        return n * 2
    else:
        return n * n

#Problem 4
def add_two_to_alternate_elements(t: tuple) -> tuple:
    """
    Write a function add_two_to_alternate_elements(t) that takes a tuple of integers with
    at least one element and returns a new tuple in which 2 has been added to every
    element at an even index (0, 2, 4, ...). The elements at odd indices stay the same.

    Examples:
    add_two_to_alternate_elements((1, 2, 3, 4, 5)) -> (3, 2, 5, 4, 7)
    add_two_to_alternate_elements((10, 20)) -> (12, 20)
    """
    result = []
    for index, value in enumerate(t):
        if index % 2 == 0:
            value += 2
        result.append(value)

    return tuple(result)

#problem 5
dimension = input().split()
m = int(dimension[0])
n = int(dimension[1])

max_sum = None
max_index = 0

for i in range(m):
    row = input().split()
    current_sum = 0
    for num in row:
        current_sum += int(num)

    if max_sum is None or current_sum > max_sum:
        max_sum = current_sum
        max_index = i

print(max_index)
print(max_sum)
