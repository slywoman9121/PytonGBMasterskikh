user_name = input('What is your name? - ')
print(f"Hi, {user_name}")
my_file = open("FirstFile.txt", "w+")
# my_file.write(f"HI, {user_name}!")
while tt := input("Введите текст - "):
    with open("FirstFile.txt", "a") as file3:
        file3.write(f"\n{tt}")
