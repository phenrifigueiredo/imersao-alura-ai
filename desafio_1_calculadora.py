# ==========================================
# 1. FUNÇÕES DAS OPERAÇÕES MATEMÁTICAS
# ==========================================
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Proteção contra divisão por zero
    if b == 0:
        return None
    return a / b

def potencia(a, b):
    return a ** b

def porcentagem(valor, taxa):
    """Calcula 'taxa'% sobre o 'valor'."""
    return (valor * taxa) / 100

# ==========================================
# 2. FUNÇÃO AUXILIAR PARA ENTRADA DE NÚMEROS
# ==========================================
def pedir_numeros():
    """Pede os dois números ao usuário evitando repetição de código."""
    n1 = float(input('Escolha o primeiro número: '))
    n2 = float(input('Escolha o segundo número: '))
    return n1, n2

# ==========================================
# 3. PROGRAMA PRINCIPAL
# ==========================================
def main():
    nome = input('Qual é o seu nome? ').strip()
    print(f'Muito prazer, {nome}!')

    while True:
        print('\n' + '=' * 20)
        print('    CALCULADORA')
        print('=' * 20)
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Potenciação')
        print('6 - Porcentagem')
        print('0 - Sair')
        print('=' * 20)

        escolha = input(f'{nome}, escolha uma opção (0 a 6): ').strip()

        if escolha == '0':
            print(f'Até mais, {nome}! Obrigado por usar a calculadora.')
            break

        elif escolha == '1':
            print('\nSua escolha foi ADIÇÃO.')
            n1, n2 = pedir_numeros()
            resultado = somar(n1, n2)
            print(f'{nome}, a soma entre eles é {resultado:.2f}.')

        elif escolha == '2':
            print('\nSua escolha foi SUBTRAÇÃO.')
            n1, n2 = pedir_numeros()
            resultado = subtrair(n1, n2)
            print(f'{nome}, a subtração entre eles é {resultado:.2f}.')

        elif escolha == '3':
            print('\nSua escolha foi MULTIPLICAÇÃO.')
            n1, n2 = pedir_numeros()
            resultado = multiplicar(n1, n2)
            print(f'{nome}, a multiplicação entre eles é {resultado:.2f}.')

        elif escolha == '4':
            print('\nSua escolha foi DIVISÃO.')
            n1, n2 = pedir_numeros()
            resultado = dividir(n1, n2)
            if resultado is None:
                print('Erro: Não é possível dividir por zero!')
            else:
                print(f'{nome}, a divisão entre eles é {resultado:.2f}.')

        elif escolha == '5':
            print('\nSua escolha foi POTENCIAÇÃO.')
            n1, n2 = pedir_numeros()
            resultado = potencia(n1, n2)
            print(f'{nome}, a potenciação entre eles é {resultado:.2f}.')

        elif escolha == '6':
            print('\nSua escolha foi PORCENTAGEM.')
            valor_base = float(input('Digite o valor total (ex: 200): '))
            taxa = float(input('Digite a porcentagem desejada (ex: 15 para 15%): '))
            resultado = porcentagem(valor_base, taxa)
            print(f'{nome}, {taxa:.2f}% de {valor_base:.2f} é {resultado:.2f}.')

        else:
            print('Opção inválida! Por favor, escolha um número de 0 a 6.')

if __name__ == '__main__':
    main()
