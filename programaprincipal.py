def obter_numero(mensagem):
    """Função para obter um número inteiro do usuário com uma mensagem personalizada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


def exibir_tabuada(numero):
    """Função para exibir a tabuada de um número fornecido."""
    print(f"\nTabuada de {numero}:")
    for c in range(0, 11):
        print(f'{c} X {numero} = {c * numero}')


def main():
    """Função principal que executa o programa de tabuada."""
    while True:
        n1 = obter_numero('Quer ver a tabuada de qual valor? ')

        # Exibe a tabuada do número fornecido
        exibir_tabuada(n1)

        # Solicita um novo número para a tabuada ou um número negativo para encerrar
        n1 = obter_numero('Escolha outro número positivo para tabuada ou um negativo para encerrar o programa: ')

        # Verifica se o número é negativo para encerrar o loop
        if n1 < 0:
            break

    # Mensagem de encerramento
    print('Encerrado')


if __name__ == "__main__":
    main()
