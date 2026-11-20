# OPPE1 Set2 May 2025
#Problem 1
def is_even_or_divisible_by_5(num: int) -> bool:
    """
    Given an integer, check if a number is either even or divisible by 5.

    Eg.
    is_even_or_divisible_by_5(8) -> True
    is_even_or_divisible_by_5(10) -> True
    is_even_or_divisible_by_5(15) -> True
    is_even_or_divisible_by_5(7) -> False

    Args:
        num (int): An integer.

    Returns:
        bool: True if even or if divisible by 5 else False.
    """
    if num % 2 == 0 or num % 5 == 0:
        return True
    else:
        return False



#Section 1  problem 3
def make_dict_from_elems_in_index(keys, values, index: int) -> dict:
    """
    Returns a dictionary with one key and value pair
    taken from the given index of keys and values list.

    Eg:
    >>> keys = ['apple', 'banana', 'cherry']
    >>> values = [10, 20, 30, 40]
    >>> make_dict_from_elems_in_index(keys, values, 1)
    {'banana': 20}
    >>> make_dict_from_elems_in_index(keys, values, -1)
    {'cherry': 40}

    Args:
        keys (list): The list with the keys.
        values (list): The list with the values.
        index (int): An integer

    Returns:
        dict: Dictionary with only one key-value pair, where the key and value are taken from the given index.
    """
    keys = keys[index]
    values = values[index]
    return {keys: values}



#Section 2 Problem 1
def count_unique_even_odd(l: list) -> dict:
    '''Returns a dict with the count of unique even and odd numbers in the list.

    Eg.
    >>> l = [1, 2, 2, 3, 4, 5, 5, 6]
    >>> count_unique_even_odd(l)
    {"even": 3, "odd": 3}

    Args:
        l(list) : a list of integers.

    Returns:
        dict: a dict with the count of unique even and odd numbers in the list.
    '''
    l1 = []
    even = 0
    odd = 0
    for elem in l:
        if elem % 2 == 0 and elem not in l1:
            even += 1
            l1.append(elem)
        if elem % 2 != 0 and elem not in l1:
            odd += 1
            l1.append(elem)

    return {"even": even, "odd": odd}



#section 2 Problem 2
sen = input()
words = sen.split()
for elem in words:
    count = 0
    for ch in elem:
        if ch in "aeiouAEIOU":
            count += 1
    print(f"{elem}{count}", end=" ")


#Section 3 Problem 1
def filter_students(data, criteria):
    """
    Filters names based on the given criteria:
    - "excellent" - average score >= 85.
    - "good" - average score >= 50 and < 85.
    - "all_pass" - all scores >= 50.
    - "balanced" - difference between min and max is <= 10.

    Args:
        data (dict): keys are student names and values are lists of scores
        criteria (str): filtering condition

    Returns:
        set: Set of student names matching the criteria
    """
    result = set()
    for name, scores in data.items():
        avg = sum(scores) / len(scores)
        if criteria == "excellent":
            if avg >= 85:
                result.add(name)
        elif criteria == "good":
            if 50 <= avg < 85:
                result.add(name)
        elif criteria == "all_pass":
            if min(scores) >= 50:
                result.add(name)
        elif criteria == "balanced":
            if max(scores) - min(scores) <= 10:
                result.add(name)
    return result

    
     
