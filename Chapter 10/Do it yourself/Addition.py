print("Provide me two numbers and i'll add it for you")
print("Enter 'q' to quit")

while True:
    first_input = input("First Number: ")
    if first_input == 'q':
        break
    second_input = input("Second Number: ")
    if second_input == 'q':
        break
    try:
        first_number = int(first_input)
        second_number = int(second_input)
    except ValueError:
        print("Please enter integer value only.")
    else:
        answer = first_number + second_number
        print(answer)


