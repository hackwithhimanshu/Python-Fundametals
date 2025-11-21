class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of this restaurant is {self.restaurant_name}")
        print(f"It is {self.cuisine_type} style restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open")

restaurant = Restaurant('Kiminatsu', 'Japanese')
restaurant_two = Restaurant('Dhillons', 'Indian')
restaurant_three = Restaurant('Baritotu', 'Italian')


restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
