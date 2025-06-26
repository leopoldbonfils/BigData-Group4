def calculate_age(year_of_birth):
    current_year = 2025
    return current_year - year_of_birth

name = input("Please enter your name: ")
year = int(input("Enter your year of birth (e.g., 2000): "))

age = calculate_age(year)
print(f"\nThank you {name}, your age is: {age}")