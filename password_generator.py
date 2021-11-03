import random


def generate_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '=', '_', '^', '~', '`', '{', '}', '|']
    caracteres = mayusculas + minusculas + numbers + symbols

    password = []
    contador = 0

    while contador < 15:
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)
        contador += 1

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print('New password: ' + password)


if __name__ == '__main__':
    run()
