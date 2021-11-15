user_name = input('What is your name? - ')
users_time_s = int(input("Enter the running time in seconds - "))
if users_time_s > 59:
    user_time_h = int(users_time_s // 3600)
    user_time_m = int(users_time_s % 3600)
    user_time_m = int(user_time_m // 60)
    users_time_s = int(users_time_s % 60)
print (f"Hi, {user_name}! Your running time:{user_time_h:02}:{user_time_m:02}:{users_time_s:02}")