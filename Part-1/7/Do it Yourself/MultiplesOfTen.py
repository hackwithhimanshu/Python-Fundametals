num = input("Enter a number i'll tell you if its multiple of 10 or not.\n-> ")
num = int(num)

if num % 10 == 0:
    print(f"{num} is multiple of 10")
else:
    print(f"{num} is not a multiple of 10")