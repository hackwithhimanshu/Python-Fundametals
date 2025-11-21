from random import sample

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

my_ticket = [10, 'a', 5, 'c']

count = 0
winner = None

while winner != my_ticket:
    winner = sample(lottery_values, 4)
    count += 1

print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winner}")
print(f"It took {count} to win the lottery.")


