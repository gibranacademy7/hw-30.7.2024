def zugi_print(numbers) -> None:
    """
    The purpose of the zugi_print function is to iterate through
    a list of numbers and print whether each number is even or odd.
    Here's a step-by-step explanation of how it works:
    """
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} = even");
        else:
            print(f"{number} = odd");
