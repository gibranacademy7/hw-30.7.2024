### Collect scores from the user, validate them, and call a function to display statistics
from func_without_return_1e import my_statistics


def get_scores():
    scores = [];
    while True:
        try:
            score = float(input("Enter a score (-99 to end): "));
            if score == -99:
                break
            if 0 <= score <= 100:
                scores.append(score);
            else:
                print("Score must be between 0 and 100.");
        except ValueError:
            print("Invalid input. Please enter a numeric value.");
    return scores;


def main():
    scores = get_scores();
    my_statistics(scores);


if __name__ == "__main__":
    main();
help(my_statistics);

