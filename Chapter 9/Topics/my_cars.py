# from car import Car, Electric_class

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = Electric_class('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

import car
from my_electric_car import Electric_class as EC

my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

