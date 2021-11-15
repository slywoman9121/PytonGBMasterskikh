user_name = input('What is your name? - ')
user_year = int(input("How old are you - "))
user_number = int(input("Enter your personal number: "))
cabinet = int(input("Enter the cabinet number: "))
cy = 2021
user_y = int(cy-user_year)

h = (f"Hi, {user_name}. Your year of birth: {user_y}")
n = (f"Your personal number {user_number:03} and your cabinet number {cabinet:04}")

print(h)
print(n)
