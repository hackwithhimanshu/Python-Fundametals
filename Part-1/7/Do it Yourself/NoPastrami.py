sandwich_orders = ['cheese corn sandwich', 'pastrami sandwich', 'bombay masala sandwich', 'pastrami sandwich', 'tadoori paneer sandwich', 'pastrami sandwich', 'loaded veggie sandwich']
finished_sandwiches = []

sandwich_active = True
print("We are sorry to inform you\ndeli has runout of pastrami sandwich.")

                

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
    
while sandwich_orders:   
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print(f"\nI made your {sandwich_order}")

print("\n---Copleted Orders----")
for sandwich in finished_sandwiches:
        print(sandwich.title())