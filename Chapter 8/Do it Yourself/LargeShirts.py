def make_shirt(tshirt_size='L', tshirt_print='I love python'):
    print(f"T-Shirt size is {tshirt_size.upper()}")
    print(f"T-Shirt Print is {tshirt_print.title()}")

make_shirt()
make_shirt('M')
make_shirt(tshirt_print='Python is great', tshirt_size='S')