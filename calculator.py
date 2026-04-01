"""A simple calculator that perfoms additon and multiplication
"""


def get_numbers():
    """Get numbers from user input.
    """
    numbers = []
    print("Enter numbers (Type 'done' when finished): ")
    while True:
        user_input = input("Enter a number: ").strip()
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number")
    return numbers


def add_numbers(numbers):
    pass


def main():
    """
    main function to run the calculator
    """
    print("=" * 50)
    print("WELCOME TO THE CALCULATOR!")
    print("=" * 50)

    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered exiting")
        return
    print(f"\n You entered: {numbers}")
    print("\n What opertaions would you like to perform?")
    print("1. Add \n 2. Mulitply")

    choice = input("Enter your choice (1 or 2): ")

    # Operations will be implemented by Chrisitine and Tricket
    if choice == "1":
        print("Addition feature coming soon")
        # TODO: Tricket to implement this
    elif choice == "2":
        print("Multiplication feature coming soon")
        # TODO: Christine to implement this
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
