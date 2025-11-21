from cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras: list):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


def main():
    print("proceso de cálculo aplicado a las figuras geométricas")


    c1 = Cuadrado(6)
    c2 = Cuadrado(5)

    r1 = Rectangulo(8, 7)
    r2 = Rectangulo(3, 12)

    figuras = [c1, c2, r1, r2]


    for f in figuras:
        print(f)
        print(f"El Área es: {f.area()}")
        print(f" El Perímetro es: {f.perimetro()}")


    print("Prueba de ejecución para los errores")
    try:
        c3 = Cuadrado(-6)
    except ValueError as l:
        print("Error", l)

    try:
        r3 = Rectangulo(0, 4)
    except ValueError as l:
        print(l)



    print("Suma de areas y perimetros")
    print("la suma de todas las areas:", sumar_areas(figuras))
    print("la suma de todos los perímetros:", sumar_perimetros(figuras))


if __name__ == "__main__":
    main()