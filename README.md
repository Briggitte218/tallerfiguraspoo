DESCRIPCIÓN DEL EJERCICIO
​El objetivo es crear un sistema organizado de clases para representar figuras geométricas, específicamente un Cuadrado y un Rectángulo, y asegurar que estas clases funcionen correctamente y sigan las buenas prácticas de programación.
Conceptos de POO que se Usarán
​Este taller se enfoca en demostrar tu habilidad para implementar los siguientes pilares de la POO:
​Herencia: Crear una clase base general llamada FiguraGeometrica y hacer que las clases específicas (Cuadrado y Rectangulo) hereden sus características y comportamientos.
​Encapsulamiento: Proteger los datos internos de las figuras (como sus lados o dimensiones) usando propiedades privadas y controlando cómo se acceden o modifican mediante decoradores especiales (@property y setters). Esto también incluye validaciones internas para asegurar que los datos ingresados sean lógicos (por ejemplo, que los lados sean positivos).
​Sobrescritura de Métodos: Modificar el comportamiento de los métodos heredados. Por ejemplo, cada figura tendrá su propia manera de calcular el área y el perímetro, y se personalizará el método especial __str__ para una impresión legible de sus detalles.
​Polimorfismo: Asegurar que un mismo método (como calcular_area()) se comporte de manera diferente según la figura a la que se aplique (un cuadrado o un rectángulo).
Estructura del Proyecto
​Deberás tener al menos dos partes:
​Clases de las Figuras: Los archivos con la definición de las clases FiguraGeometrica, Cuadrado y Rectangulo.
​Archivo Principal (main.py): Un archivo donde se crearán instancias de las clases (Cuadrado y Rectangulo) para probar y demostrar que todos los cálculos (área, perímetro) y las validaciones funcionan correctamente.
EXPLICACIÓN DE CADA CLASE 
La clase FiguraGeometrica es la clase padre de todas las figuras. Su función es definir atributos y comportamientos básicos que comparten todas las figuras geométricas, como el alto y el ancho. En esta clase también se hacen validaciones para evitar que los valores sean menores o iguales a cero. Además, contiene un método general para calcular el área, aunque normalmente será reemplazado por las clases hijas. El método del perímetro queda vacío para que cada figura lo defina según sus necesidades. También tiene un método str que muestra la información de la figura.
La clase Rectangulo hereda de FiguraGeometrica. Representa específicamente un rectángulo y por eso utiliza el ancho y el alto que la clase padre ya maneja. Sobrescribe el método area para calcularla multiplicando el ancho por el alto y también sobrescribe el método perimetro para devolver la fórmula correcta del rectángulo. Su método str muestra información específica del rectángulo.
La clase Cuadrado también hereda de FiguraGeometrica, pero a diferencia del rectángulo, solo necesita un valor: el lado. Por eso, al crear un cuadrado, se envía el mismo valor como alto y ancho a la clase padre. El método area calcula el lado multiplicado por sí mismo y el método perimetro lo calcula multiplicando el lado por cuatro. En su método str muestra la información del cuadrado.
La clase Triangulo (si la estás usando) también hereda de FiguraGeometrica. Aquí, el ancho se utiliza como base y el alto como altura. Su método area calcula el área como base por altura dividido para dos. El método perimetro depende de los lados del triángulo y puede implementarse de diferentes maneras según el diseño. Su método str muestra los valores que representan al triángulo.
CAPTURA DE LA EJECUCUIÓN 
![WhatsApp Image 2025-11-21 at 1 25 19 AM](https://github.com/user-attachments/assets/59d18781-39d3-4e51-98d2-74d82fb2bfcf)
