# prompt = "Enter the toppings for piiza\n"
# prompt += "write 'quit' as you finish\n-> "

# topping = ""

# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"{topping} is added")
#     else:
#         print("Thankyou, food will be ready soon\nPlease take your seat")

prompt = "Enter the toppings for piiza\n"
prompt += "write 'quit' as you finish\n-> "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"{topping} is added")