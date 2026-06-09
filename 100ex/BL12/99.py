class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

ret = Retangulo(base, altura)

print("Área:", ret.area())
print("Perímetro:", ret.perimetro())