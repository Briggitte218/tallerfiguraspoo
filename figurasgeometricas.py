'''
código para calcular el area y el perímetro de las figuras geométricas
'''
class FiguraGeometrica:
    def __init__(self, alto: float, ancho:float):
       self.alto = alto
       self.ancho = ancho

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
        #validacion para que el valor sea mayor que 0
           raise ValueError('el ancho tiene un valor superior a 0')
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            # validacion para que el valor sea mayor que 0
           raise ValueError('El alto debe tener un valor superior a 0')
        self._alto = valor

    def area(self):
      return self.ancho * self.alto
    def perimetro(self):
        pass
    def __str__(self):
       return f' El alto de la figura es: {self.alto}, y el ancho es: {self.ancho}'