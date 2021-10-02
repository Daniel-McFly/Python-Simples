nome = input('digite seu nome: ')
print('Bem vindo {}!' . format(nome))
aprov = 'não aprovado'

def calc():
    print('\n\n----calculadora----')
    print('Soma = 1\nSubtração = 2\nMultipliação = 3\nDivisão = 4')
    op = input('escolha uma opção: ')
    n1 = int(input('número 1: '))
    n2 = int(input('número 2: '))

    if op == '1':
        r = n1+ n2
        print('A soma é: ',r)
    elif op == '2':
        r = n1 -n2
        print('A subtração é:',r)
    elif op == '3':
        r = n1 * n2
        print('A multiplicação é:', r)
    elif op == '3':
        r = n1 / n2
        print('A divisão é:', r)
    elif op == '5' and nome == 'Daniel':
        print('ATIVADO')
        r = n1 + n2 - n1 * n2 / n1
        print('A resultado é:', r)
    else:
        print('comando inválido')
    return

if nome == 'Daniel':
    print('Você é meu criador :)')
    calc()
elif nome!= 'Daniel':
    print('Desculpe- me {}, mas infelizmente você não tem acesso a mais funções' . format(nome))






