cat_attributes = {
    "intelligence": 20,
    "energy": 15,
    "weight": 20,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name: ")

colours = ["Black","Ginger","White"]
colour = input("Enter the colour of your cat: ")
while colour not in colours:
    print("Invalid colour")
    colour = input("Enter the colour of your cat: ")

while True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Feed your cat 4. Put your cat to sleep 5. Show stats ")

    if option == '1':
        cat_attributes["intelligence"] -= 5
        cat_attributes["energy"] += 5
        cat_attributes["weight"] -= 1
        pass
    elif option == '2':
        cat_attributes["intelligence"] += 6
        cat_attributes["energy"] -= 2
        cat_attributes["weight"] -= 3
        pass
    elif option == '3':
        cat_attributes["intelligence"] += 1
        cat_attributes["energy"] += 2
        cat_attributes["weight"] += 4
        pass
    elif option == '4':
        if cat_attributes["energy"] < 20:
            cat_attributes["intelligence"] -= 1
            cat_attributes["energy"] += 10
            cat_attributes["weight"] += 3
        else:
            print("Your cat has too much energy to fall asleep")
        pass
    elif option == '5':
        print(cat_attributes)
    else:
        pass

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