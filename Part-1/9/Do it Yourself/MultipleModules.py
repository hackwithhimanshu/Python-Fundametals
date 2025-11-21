from Users import User
from Admin import Admin

user_admin_1 = Admin('Himanshu', 'Kumbhaj')
user_normal_1 = User('Akriti', 'Dixit')

user_admin_1.show_privileges()
user_normal_1.describe_user()