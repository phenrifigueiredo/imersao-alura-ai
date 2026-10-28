nome = str(input('Qual é o seu nome? '))
print(f'Muito prazer, {nome}!')
print('CALCULADORA')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potenciação')

while True:

    escolha = int(input(f'{nome}, escolha um número de 1 até 5: ').strip())[0]

    if escolha == 1:
        print('Sua escolha foi ADIÇÃO.')
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print(f'{nome}, a soma dentre eles é {n1+n2:.2f}.')

    elif escolha == 2:
        print('Sua escolha foi SUBTRAÇÃO.')
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print(f'{nome}, a subtração dentre eles é {n1-n2:.2f}.')

    elif escolha == 3:
        print('Sua escolha foi MULTIPLICAÇÃO.')
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print(f'{nome}, a multiplicação dentre eles é {n1*n2:.2f}.')

    elif escolha == 4: 
        print('Sua escolha foi DIVISÃO.')
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print(f'{nome}, a divisão dentre eles é {n1/n2:.2f}.')

    elif escolha == 5:
        print('Sua escolha foi POTENCIAÇÃO.')
        n1 = float(input('Escolha um número: '))
        n2 = float(input('Escolha outro número: '))
        print(f'{nome}, a potenciação dentre eles é {n1**n2:.2f}.')

    else:
        print('Número incorreto.')
