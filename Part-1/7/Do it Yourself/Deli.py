sandwich_orders = ['cheese corn sandwich', 'bombay masala sandwich', 'tadoori paneer sandwich', 'loaded veggie sandwich']
finished_sandwiches = []

sandwich_active = True

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print(f"I made your {sandwich_order}")

print("\n---Copleted Orders----")
for sandwich in finished_sandwiches:
        print(sandwich.title())