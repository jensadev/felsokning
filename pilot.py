print('Extra lyxig miniräknare')
while True:
    num1 = input('Skriv in tal 1: ')
    num2 = input('Skriv in tal 2: ')

    menu = input('Tryck A för att addera och M för multiplikation')

    if menu == 'A':
        print(num1 + num2)
    else:
        print(int(num1) * int(num2))
