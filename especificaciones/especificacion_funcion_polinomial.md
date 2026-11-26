# Especificación de la clase FuncionPolinomial

Archivo donde va: clases/funcion_polinomial.py

## 1. Identificación de la clase

**Nombre:** FuncionPolinomial

**Objetivo:** Representar la función que voy a integrar y saber darme su valor en cualquier
punto x

**Responsabilidad:** Esta clase solo sabe de la función Guarda sus coeficientes, se evalúa
en un punto y se escribe en texto No sabe nada de integrales, ni de intervalos, ni de
rectángulos, ni le pide datos al usuario

La separé así porque la función existe sola, sin importar qué le vaya a hacer después Es el
paso 4 de mi procedimiento (expresar f(x) en términos de x_i), y ese paso no necesita saber
de dónde salió la x

## 2. Atributos

- coeficientes -> list[float] -> Los coeficientes del polinomio, del término de mayor potencia al independiente -> Se recibe en el constructor, no tiene valor por defecto
- grado -> int -> El grado del polinomio -> Se calcula solo en el constructor como len(coeficientes) - 1

Ejemplo de cómo se guarda f(x) = x + 3:

```
coeficientes = [1, 3]
grado = 1
```

Y f(x) = 2x² - 3x + 1 se guardaría así:

```
coeficientes = [2, -3, 1]
grado = 2
```

## 3. Constructor __init__

**Qué recibe:** self y coeficientes (una lista de números)

**Qué hace:**

1. Revisa que coeficientes sea una lista y que no esté vacía Si está mal, lanza ValueError
2. Revisa que todos los elementos sean int o float Si alguno no lo es, lanza ValueError
3. Guarda la lista en self.coeficientes
4. Calcula self.grado como len(self.coeficientes) - 1

**Por qué valido aquí:** Porque si dejo pasar una lista con basura, el error va a salir
después dentro del ciclo de la suma de Riemann y ahí no voy a entender de dónde vino

## 4. Métodos

### evaluar(self, x)

**Objetivo:** Darme el valor de f(x) para una x cualquiera

**Entradas:** x, un número (int o float)

**Atributos que usa:** self.coeficientes y self.grado

**Algoritmo:**

```
resultado = 0
potencia = self.grado
recorrer cada coeficiente de la lista:
    resultado = resultado + coeficiente * (x ** potencia)
    potencia = potencia - 1
devolver resultado
```

**Resultado:** un float con el valor de f(x)

**Validaciones:** Si x no es un número, lanza TypeError

**Comprobación:** con coeficientes [1, 3] y x = -1, debe dar 2, porque f(-1) = -1 + 3 = 2

### a_texto(self)

**Objetivo:** Escribir la función de forma que se entienda al leerla, tipo f(x) = x + 3

**Entradas:** ninguna, solo self

**Atributos que usa:** self.coeficientes y self.grado

**Algoritmo:**

```
partes = lista vacia
potencia = self.grado
recorrer cada coeficiente:
    si el coeficiente es 0, saltarlo y bajar la potencia
    armar el texto del termino segun la potencia:
        potencia 0  -> solo el numero
        potencia 1  -> el numero y una x
        potencia > 1 -> el numero, una x y ^potencia
    si el coeficiente vale 1 o -1 y la potencia no es 0, no escribir el 1
    agregar el termino a partes
    potencia = potencia - 1
unir las partes poniendo + o - segun el signo
devolver "f(x) = " mas lo unido
```

**Resultado:** una cadena de texto

**Validaciones:** Si todos los coeficientes son 0, devuelve f(x) = 0

**Comprobación:** con [1, 3] debe dar f(x) = x + 3, y con [2, -3, 1] debe dar
f(x) = 2x^2 - 3x + 1

## 5. Reglas que no se pueden cambiar

- **RF1** La lista va de mayor a menor potencia, nunca al revés Si se invierte, el polinomio
  deja de ser el mismo
- **RF2** evaluar no redondea ni recorta decimales El redondeo es cosa de cuando se imprime,
  no del cálculo
- **RF3** a_texto solo arma texto, no calcula nada
- **RF4** La clase nunca usa input ni print Todo lo que entra viene por parámetros y todo lo
  que sale es con return El que habla con el usuario es main.py
- **RF5** No se agregan métodos de derivada, antiderivada ni integración a esta clase Esta
  clase es la función y nada más
