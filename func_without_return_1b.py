def my_details(str) -> str:
    """
    Prints the first, middle, and last characters of a given string.
    """
    first_char = str[0];
    middle_char = str[len(str) // 2];
    last_char = str[-1];

    print("1st char is: ", first_char);
    print("Middle char is: ", middle_char);
    print("Last char is: ", last_char);
