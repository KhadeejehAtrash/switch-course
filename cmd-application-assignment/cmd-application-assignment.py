def check_palindrome(user_input):
    if user_input == user_input[::-1]:
        print("Result: The input is a palindrome")
    else:
        print("Result: The input is NOT a palindrome")

def check_lowercase(user_input):
    if user_input.islower():
        print("Result: All characters are lowercase")
    else:
        print("Result: Not all characters are lowercase")

def check_digits(user_input):
    if user_input.isdigit():
        print("Result: All characters are digits")
    else:
        print("Result: Not all characters are digits")

def check_length(user_input):
    if len(user_input) > 15:
        print("Result: The input is longer than 15 characters")
    else:
        print("Result: The input is 15 characters or shorter")

def check_empty(user_input):
    if not user_input:
        print("Result: The input is empty")
    else:
        print("Result: The input is NOT empty")


def main():
    while True:
        menu_text = """
===============================
Available Operations:
1- Palindrome: check if the input palindrome " 
2- Lower: check if all characters in the input are lowercase" 
3- Digit: check if all characters in the input are digits 
4- Long: check if the input length is longer than 15 
5- Empty: check if th input is empty 
6- Exit: Exit successfully from the application 
===============================
"""
        print(menu_text)

        try:
            menu_number = int(input("Enter the number of the operation you choose: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.\n")
            continue

        if menu_number == 6:
            print("Exiting the program. Goodbye!")
            break

        if menu_number in [1, 2, 3, 4, 5]:
            user_input = input("Enter input: ")

            if menu_number == 1:
                check_palindrome(user_input)
            elif menu_number == 2:
                check_lowercase(user_input)
            elif menu_number == 3:
                check_digits(user_input)
            elif menu_number == 4:
                check_length(user_input)
            elif menu_number == 5:
                check_empty(user_input)
        else:
            print("Invalid choice! Please select a number from 1 to 6.\n")
            
            
        print("\n" + "-"*60 + "\n")


if __name__ == "__main__":
    main()
