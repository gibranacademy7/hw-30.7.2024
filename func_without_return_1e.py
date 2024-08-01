import math

### Purpose: Define the statistics_my function to process and print statistics about a list of scores.
def my_statistics(scores) -> None:
    """
    This code defines a function to calculate and print various statistics
    about a list of scores and provides a help function to describe its usage
    """
    if not scores:
        print("No scores provided.");
        return

    highest = max(scores);
    lowest = min(scores);
    count = len(scores);
    average = sum(scores) / count;

    # Calculate standard deviation
    variance = sum((x - average) ** 2 for x in scores) / count;
    stddev = math.sqrt(variance);   ### The standard deviation is simply the square root of the variance.
    ### This function from Python's math module computes the square root of x.
    """
    Example: Suppose we have a list of scores: [3, 7, 5]
    Calculate the Mean (average): (3+7+5)/3 = 5
    Calculate the Variance:
    for 3: (3-5)**2 = 4
    for 7: (7-5)**2 = 4
    for 5: (5-5)**2 = 0
    variance = (4+4+0)/3 = 8/3 (≈ 2.67)
    Standard deviation: 
    stddev = The square root of 2.67 (≈ 1.63)
    """
# Calculate outstanding and failing scores
    excellent = sum(1 for x in scores if x > 90);  # כמה ציונים מצטיינים היו מעל 90
    failing = sum(1 for x in scores if x < 55);  # כמה נכשלים היו מתחת ל- 55


    print(f"Highest score: {highest:.2f}");
    print(f"Lowest score: {lowest:.2f}");
    print(f"Number of scores: {count}");
    print(f"Average score: {average:.2f}");
    print(f"Standard deviation: {stddev:.2f}");
    print(f"Number of excellent scores: {excellent}");
    print(f"Number of failing scores: {failing}");


def help():
    print("my_statistics(scores) - \
    This function calculates and prints statistics from the provided list of scores.");
    print(
        "It prints the highest score, lowest score, number of scores, average score, standard deviation, \
        number of outstanding scores (above 90), and number of failing scores (below 55).");


if __name__ == "__main__":
    help();
