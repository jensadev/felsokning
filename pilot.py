print('Extra lyxig miniräknare')
while True:
    num1 = input('Skriv in tal 1: ')
    num1 = input('Skriv in tal 2: ')

    menu = input('Tryck [A]ddition, [D]ivision, [M]ultiplikation, [E]xit')

    if menu == 'A':
        print(num1 + num2)
    elif menu == 'D':
        print(num1 % num2)
    else:
        print(int(num1) * int(num2))
