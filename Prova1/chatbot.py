import re as regex

def get_input():
    return input("Qual a sua intenção? ")

def print_result(x):
    print("Resposta formulada:", x)

intencoes = {
    r"(pagamento|atualizar|cartão|cartao)": "pagamento",
    r"(status|onde|pedido)": "status"
}

acoes = {
        "pagamento": "Você quer pagar",
        "status": "Você quer ver o status do pedido"
        }

def main():
    while True:
        input_value = get_input()
        if input_value == "sair":
            break
        for key, value in intencoes.items():
            pattern = regex.compile(key)
            result = pattern.findall(input_value)
            result = ' '.join(result)
            if result in acoes:
                print(acoes[result])

if __name__ == '__main__':
    main()