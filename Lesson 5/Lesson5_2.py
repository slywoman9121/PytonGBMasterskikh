user_name = input('What is your name? - ')
print(f"Hi, {user_name}")
with open('SecondFile.txt') as str:
    pr = sum(1 for i in str)
    print(f"Count str - {pr}")
    with open("SecondFile.txt", "r") as file1:
        for line in file1:
            print(line.strip())
            kar = len(line) - line.count(" ")
            print(f"Count symbol - {kar}")
# Я понять не могу почему показывает кроме последней строки все на 1 символ больше

