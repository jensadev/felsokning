menu = 0

while menu:
    inventory = []
    menu = input(
        "1. Add to inventory \n2. List inventory \n3. Remove from inventory \n4. Exit \n")
    if menu == 1:
        print("Add item to inventory")
        inventory.append(input("Enter item: "))
    elif menu == 2:
        print("List inventory")
        # Lägg till så att loopen hamnar out of bounds? Indexfel
        for item in inventory:
            print(item)
    elif menu == 3:
        print("Remove item from inventory")
        # Hitta på någon ondska här? Indexfel
        inventory.remove(input("Enter item: "))
    elif menu == 4:
        print("Exit")
    else:
        print("Invalid input")
