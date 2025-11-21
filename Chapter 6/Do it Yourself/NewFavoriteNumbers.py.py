fav_num = {
    'naruto' : [2, 3],
    'kakashi' : [7, 5], 
    'minato' : [9, 5, 0],
    'jiraya' : [3, 5, 1],
    'sasuke' : [1, 5, 8],
}

for name, num in fav_num.items():
    print(f"{name}'s favorite numbers are:-")
    for fav in num:
        print(f"\t{fav}")
    print("-" * 20)

