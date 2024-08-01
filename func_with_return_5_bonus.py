def get_int(prompt_str) -> str:
    while True:
        try:
            # קלט מהמשתמש עם המחרוזת שניתנה כפרמטר
            user_input = input(f"{prompt_str}: ");
            # המרת הקלט למספר שלם
            number = int(user_input);
            # החזרת המספר התקין
            return number;
        except ValueError:
            # טיפול במקרה שהקלט לא ניתן להמרה למספר שלם
            print("The input is incorrect. Try again!");

# דוגמה לשימוש בפונקציה
number = get_int("Enter an integer number!");
print(f"The number entered is: {number}");
