guests = ['Rohan', "Mohan", "Sohan", "Ramesh"]

living_guests = 'Rohan'
diseased_guests = 'Ramesh'

guests.remove(diseased_guests)

print(f"Guests i'll invite are {guests}")

print(f"{guests[2]} won't be able to make it to the party")

guests[2] = "Goku"

print(f"People whow are coming to party are {guests}")

print(f"We have found bigger dinning table for {guests}")

guests.insert(0, "vegeta")
guests.insert(2, "beerus")
guests.append("whish")

print(f"Update!!\n people coming to the party are {guests}")

cancel_guests = guests.pop()
print(f"sorry for letting you know you are not invited! {cancel_guests}")

cancel_guests = guests.pop()
print(f"sorry for letting you know you are not invited! {cancel_guests}")

cancel_guests = guests.pop()
print(f"sorry for letting you know you are not invited! {cancel_guests}")

cancel_guests = guests.pop()
print(f"sorry for letting you know you are not invited! {cancel_guests}")

print(f"You guys are still invited {guests}")

# del guests[1]
# del guests[0]

print(guests)

print(f"no. of guests", {len(guests)})