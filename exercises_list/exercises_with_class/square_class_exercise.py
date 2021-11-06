class Quadrado:
    def __init__(self, lado=1):
        self.lado = lado

    def calcular_area(self):
        return pow(self.lado, 2)  # self.lado ** 2


quadrado = Quadrado(5)
print(quadrado.lado, quadrado.calcular_area())
