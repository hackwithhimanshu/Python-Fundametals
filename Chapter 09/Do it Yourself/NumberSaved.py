class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of this restaurant is {self.restaurant_name}")
        print(f"It is {self.cuisine_type} style restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open")

    def set_number_served(self):
        print(f"{self.number_served} people have been already served")

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('Kiminatsu', 'Japanese')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served()

restaurant.increment_number_served(5)

restaurant.set_number_served()

