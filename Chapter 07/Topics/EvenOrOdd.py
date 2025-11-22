number = input("Enter a number i'll tell you if its even or odd\n->")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")