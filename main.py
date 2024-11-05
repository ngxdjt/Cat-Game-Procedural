cat_attributes = {
    "intelligence": 20,
    "energy": 15,
    "weight": 20,
}

print("Welcome to my cat game!")

name = input("Enter name: ")

colours = ["Black","Ginger","White"]
colour = input("Enter the colour of your cat: ")
while colour not in colours:
    print("Invalid colour")
    print(f"Valid colours: {colours}")
    colour = input("Enter the colour of your cat: ")

while True:
    option = input("\nWhat would you like to do? \n1. Play with your cat \n2. Train your cat \n3. Feed your cat \n4. Put your cat to sleep \n5. Show stats\n")

    if option == '1':
        cat_attributes["intelligence"] -= 5
        cat_attributes["energy"] += 5
        cat_attributes["weight"] -= 1
        pass
    elif option == '2':
        if cat_attributes["energy"] >= 8:
            cat_attributes["intelligence"] += 10
            cat_attributes["energy"] -= 6
            cat_attributes["weight"] -= 5
        else:
            print("Your cat is too tired to train")
        pass
    elif option == '3':
        cat_attributes["intelligence"] += 2
        cat_attributes["energy"] += 2
        cat_attributes["weight"] += 5
        pass
    elif option == '4':
        if cat_attributes["energy"] <= 20:
            cat_attributes["intelligence"] -= 1
            cat_attributes["energy"] += 10
            cat_attributes["weight"] += 3
        else:
            print("Your cat has too much energy to fall asleep")
        pass
    elif option == '5':
        print(cat_attributes)
        pass
    else:
        pass
    
    print("")
    if cat_attributes['energy'] <= 5:
        print("Your cat died due to lack of energy")
        break
    elif cat_attributes["weight"] >= 50:
        print("Your cat died of obesity")
        break
    elif cat_attributes["weight"] <= 10:
        print("Your cat died of malnutrition")
        break
    elif cat_attributes["intelligence"] <= 5:
        print("Your cat died by getting hit by a car while crossing the road")
        break