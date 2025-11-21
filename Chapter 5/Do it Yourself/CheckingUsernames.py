current_users = ['admin', 'himanshu', 'akriti', 'samdarshi', 'aryan']

new_users = ['uttam', 'lobhna', 'ananya', 'SAMDARSHI', 'HIMANSHU']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} has already been used")
    else:
        print(f"{new_user} is available")