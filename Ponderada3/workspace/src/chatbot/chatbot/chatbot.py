import re as regex

def follow_point(x):
    print("Destino detectado: ", x)

intentions = {
    r"\b[Vv][áa](?:\s(?:para|ao|à))?\s?[oa]?\s(.+)": "local",
    r"\b[Mm][e](?:\s(?:leve|guie))?\s?(?:para|à|ao)?\s[oa]?\s?(.+)": "local",
}

action = {"local": follow_point}

def main():
    input_value = input("Para onde você deseja que o robô vá? ")
    for key, value in intentions.items():
        pattern = regex.compile(key)
        result = pattern.findall(input_value)
        if result:
            action[value](result[0])

if __name__ == '__main__':
    main()