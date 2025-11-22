from random import choice

lottery_values = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    'a',
    'b',
    'c',
    'd',
    'e'
]

print("Any ticket matching these 4 numbers or letters wins a prize.")

for lottery in range(4):
    lottery = choice(lottery_values)
    print(lottery)
