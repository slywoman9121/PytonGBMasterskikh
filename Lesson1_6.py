kmtr =float(input('Введите сколько километорв пробежали в первый день - '))
daypr = int(input('Введите день - '))
print (f"В первый день пробежали - {kmtr}km. Указанный день:{daypr}")
da=0
while da<daypr :
    da = da + 1
    kmtr = kmtr +(kmtr*0.1)
    print(f"{da} день вы пробежали {kmtr}km")

dd=int(kmtr)
print(F"В {da} день вы пробежали более {dd}km")
print("Program ended")
