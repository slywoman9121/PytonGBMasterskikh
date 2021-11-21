user_name = input('What is your name? - ')
print(f"Hi, {user_name}")
salary = 0
with open("ThirdFile.txt", "r") as str:
    for line in str:
        print(line.strip())
        rr = line.split()
        yy = int(rr[1])
        # ttt = str(rr[0])
        salary += int(rr[1])
        if yy < 20000:
            print(f"Minimum salary - {rr[0]}")
            # print(f"Type {type(yy)}")
    with open('ThirdFile.txt') as str:
        pr = sum(1 for i in str)
        szp=int(salary/pr)
        print(f"Average salary - {szp}")