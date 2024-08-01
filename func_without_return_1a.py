
def my_ascending(a: int, b: int) -> None:
    """
    Prints all numbers in ascending order between two given integers, inclusive.
    The function finds the minimum and maximum of the two integers and prints
    each integer from the minimum to the maximum, inclusive.
    """
    for i in range(min(a, b), max(a, b) + 1):
        print(i);

