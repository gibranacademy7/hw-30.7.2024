def zug_print(numbers) -> str:
    """
    The purpose of the zug_print function is to iterate through
    a list of numbers and return a list of strings indicating
    whether each number is even or odd.
    Here's a step-by-step explanation of how it works:
    """
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(f"{number} = even")
        else:
            result.append(f"{number} = odd")
    return result
