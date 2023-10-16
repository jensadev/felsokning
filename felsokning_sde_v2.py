# Fel lista: (Ej för eleverna?)
# scope och deklarering på inventory
# inputint returnerar fel på alla utom alternativ 1, Kan vara svårt att hitta. 
# indexfel för remove 
# Är det för få fel?
#####################################################################
menu = True

def inputInt(text):  ## Mata in menyIndex eller inventoryIndex och casta den till int
    while True:
        try:
            data = int(input(text))
            return data
        except:
            print("det blev fel")

inventory = []
while menu:
    menu = inputInt(
        "1. Add to inventory \n2. List inventory \n3. Remove from inventory \n4. Exit \n")
    if menu == 1:
        print("Add item to inventory")
        inventory.append(input("Enter item: "))
    elif menu == 2:
        print("List inventory")
        for item in inventory:
            print(item)
    elif menu == 3:
        print("Remove item from inventory")
        for key,item in enumerate(inventory):
            print((key+1),item)
        inventory.pop(inputInt("Enter itemindex: "))
    elif menu == 4:
        # menu=False Evighetsloop
        print("Exit")
    else:
        print("Invalid input")
