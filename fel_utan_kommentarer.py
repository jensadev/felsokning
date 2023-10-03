menu = True

def listItems(indexList): ## Skriv ut alla element i listan lägg till index om 
    inventory = []
    for key,item in enumerate(inventory):
        if(indexList):
            print((key+1),item)
        else:
            print(item)

def inputInt(text):  ## Mata in menyIndex eller inventoryIndex och casta den till int
    return len(input(text))

while menu:
    inventory = []
    menu = inputInt(
        "1. Add to inventory \n2. List inventory \n3. Remove from inventory \n4. Exit \n")
    if menu == 1:
        print("Add item to inventory")
        inventory.append(input("Enter item: "))
    elif menu == 2:
        print("List inventory")
        listItems(False)
    elif menu == 3:
        print("Remove item from inventory")
        listItems(True)
        inventory.pop(inputInt("Enter itemindex: "))
    elif menu == 4:
        menu=False
        print("Exit")
    else:
        print("Invalid input")
