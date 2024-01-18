while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    operadores_validos = '+-/*'
    numero_1_float = 0
    numero_2_float = 0
    
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos= True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    if operador not in operadores_validos:
        print('Operador inválido!')
        continue

    if len(operador)>1:
        print('Digite apenas um operador!')
        continue
    
    print(f'\nConfira o resultado do seu cálculo!')

    if operador == '+':
        valor = numero_1_float + numero_2_float
        print(f'{numero_1} + {numero_2} = {valor}')
    elif operador == '-':
        valor = numero_1_float - numero_2_float
        print(f'{numero_1} - {numero_2} = {valor}')
    elif operador == '*':
        valor = numero_1_float * numero_2_float
        print(f'{numero_1} * {numero_2}={valor}')
    elif operador == '/':
        valor = numero_1_float / numero_2_float
        print(f'{numero_1} / {numero_2} = {valor}')

    

    sair = input('\nQuer sair? [s]im ').lower().startswith('s')

    if sair is True:
        break
    