def is_palindrome(text):
    return text == text[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")