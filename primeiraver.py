# Solicita ao usuário um número para mostrar a tabuada
n1 = int(input('Quer ver a tabuada de qual valor? '))

while True:
    # Exibe a tabuada do número fornecido
    for c in range(0, 11):
        print(f'{c} X {n1} = {c * n1}')  # Exibe a multiplicação

    # Solicita um novo número para a tabuada ou um número negativo para encerrar
    n1 = int(input('Escolha outro número positivo para tabuada ou um negativo para encerrar o programa: '))
    
    # Verifica se o número é negativo para encerrar o loop
    if n1 < 0:
        break

# Mensagem de encerramento
print('Encerrado')
