"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    Comprar apenas latas de 18 litros;
    Comprar apenas galões de 3,6 litros;
    Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
    os valores para cima, isto é, considere latas cheias.
"""
# from math import ceil, floor


def calcular_metros_quadrados(x, y):
    if x == 0 or y == 0:
        raise ValueError("Não pode ser 0")
    return x * y


if __name__ == '__main__':
    largura = 40  # float(input("Largura: "))
    altura = 5.6  # float(input("Altura: "))
    real_m2 = calcular_metros_quadrados(largura, altura)
    increase_10 = 10/100
    coverage = 6  # six square meters per liter
    nominal_m2 = real_m2 * (1 + increase_10) / coverage
    cans = 18
    gallons = 3.6
    a, b = divmod(nominal_m2, cans)
    b, c = (divmod(b, gallons))
    print(f'latas: {a}')
    print(f'galões: {b}')

    print(f'{3.6 - c} liters to complete 1 more gallon')
