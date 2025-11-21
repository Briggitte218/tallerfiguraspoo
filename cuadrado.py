from figurasgeometricas import FiguraGeometrica

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        super().__init__(lado, lado)
    def area(self):
        return self.alto * self.alto
    def perimetro(self):
        return 4 * self.ancho
    def __str__(self):
        return f'el cuadrado tiene (lado={self.ancho})'