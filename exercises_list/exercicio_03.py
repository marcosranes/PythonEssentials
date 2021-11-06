"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

"""
nome = input("Nome: ")
if len(nome) < 4:
    raise TypeError("deve ser maior que 3 caracteres")

idade = int(input("Idade: "))
if idade < 0 or idade > 150:
    raise TypeError("entre 0 e 150")

salario = float(input("Salário: "))
if salario < 0:
    raise TypeError("must be greater than zero")

sexo = input("Sexo: ['f' ou 'm']: ")
if sexo not in 'fm':
    raise TypeError('f ou m')

estado_civil = input("Estado Civil: ['s', 'c', 'v', 'd']: ")
if estado_civil not in 'scvd':
    raise TypeError('s', 'c', 'v', 'd')
"""

"""
while True:
    try:
        nome = input("Nome: ")
    except ValueError:
        pass
    else:
        if len(nome) > 2:  # Ana should be covered!
            print("validated")
            break
        else:
            print("deve ser maior que 3 caracteres")
"""

while True:
    nome = input("Nome: ")
    if len(nome) > 2:  # Ana's case should be covered!
        print("validated")
        break
    else:
        print("deve ser maior que 2 caracteres")
