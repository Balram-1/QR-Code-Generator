def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))
        result = check_odd_even(user_input)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")
