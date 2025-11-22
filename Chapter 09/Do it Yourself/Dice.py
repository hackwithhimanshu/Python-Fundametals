from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print("\nRolling dice....")
        rolling_dice = randint(1, self.sides)
        return rolling_dice

dice_1 = Die()

for die in range(10):
    print(f"result: {dice_1.roll_die()}")

dice_2 = Die(10)

for die in range(10):
    print(f"result: {dice_2.roll_die()}")

dice_3 = Die(20)
for dice in range(10):
    print(f"result: {dice_3.roll_die()}")