class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of this restaurant is {self.restaurant_name}")
        print(f"It is {self.cuisine_type} style restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is Open")
    

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = ['chocolate', 'vanila', 'buttersotch', 'caremel']

    def greeting(self):
        print(f"Welcome to my {self.restaurant_name}")
    
    
    def ice_cream_flavours(self):
        print(f"Flavours available are:-")
        for flavor in self.flavors:
            print(f"-{flavor}")

        
icecreamshop = IceCreamStand('Kotaba Ice Creams')

icecreamshop.greeting()
icecreamshop.ice_cream_flavours()


