# Especificación de la clase FuncionPolinomial

Archivo donde va: clases/funcion_polinomial.py

## 1. Identificación de la clase

**Nombre:** FuncionPolinomial

**Objetivo:** Representar la función que voy a integrar y darme su valor en cualquier punto

**Responsabilidad:** Esta clase nada más sabe de la función Guarda sus coeficientes, se
evalúa en un punto y se escribe en texto No sabe de integrales, ni de intervalos, ni de
rectángulos, y tampoco le pide datos al usuario

Es mi paso 4, expresar f(x) en términos de x_i Ese paso no necesita saber de dónde salió la x

## 2. Atributos

- coeficientes -> list[float] -> Los coeficientes, del término más grande al independiente -> Llega por el constructor
- grado -> int -> El grado del polinomio -> Se calcula solo, con len(coeficientes) - 1

Así se guardan dos ejemplos:

```
f(x) = x + 3           ->  coeficientes = [1, 3],     grado = 1
f(x) = 2x² - 3x + 1    ->  coeficientes = [2, -3, 1], grado = 2
```

## 3. Constructor __init__

**Qué recibe:** self y coeficientes, que es una lista de números

**Qué hace:**

1. Revisa que sea una lista y que no esté vacía Si no, lanza ValueError
2. Revisa que todos sean int o float Si no, lanza ValueError Los booleanos tampoco pasan,
   porque en Python True vale 1 y se colaría sin que nadie se diera cuenta
3. Guarda la lista en self.coeficientes
4. Calcula self.grado

**Por qué valido aquí:** Si dejo pasar basura, el error va a salir después dentro del ciclo
de la suma, y ahí ya no se entiende de dónde vino

## 4. Métodos

### evaluar(self, x)

**Objetivo:** Darme el valor de f(x) para cualquier x

**Entradas:** x, un número

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

**Validaciones:** Si x no es número, lanza TypeError

**Comprobación:** con [1, 3] y x = -1 debe dar 2, porque f(-1) = -1 + 3 = 2

### a_texto(self)

**Objetivo:** Escribir la función para que se entienda al leerla, tipo f(x) = x + 3

**Entradas:** ninguna, solo self

**Atributos que usa:** self.coeficientes y self.grado

**Algoritmo:**

```
partes = lista vacia
potencia = self.grado
recorrer cada coeficiente:
    si el coeficiente es 0, saltarlo y bajar la potencia
    armar el texto del termino segun la potencia:
        potencia 0   -> solo el numero
        potencia 1   -> el numero y una x
        potencia > 1 -> el numero, una x y ^potencia
    si el coeficiente vale 1 o -1 y la potencia no es 0, no escribir el 1
    agregar el termino a partes
    potencia = potencia - 1
unir las partes poniendo + o - segun el signo
devolver "f(x) = " mas lo unido
```

**Resultado:** un texto

**Validaciones:**

- Si todos los coeficientes son 0, devuelve f(x) = 0
- Si un coeficiente viene como float pero vale entero, se escribe sin el .0, o sea que 3.0 se
  escribe 3 Esto importa porque main.py los pide con pedir_decimal y siempre llegan float
- Los que sí tienen decimales se escriben completos, como 2.5

**Comprobación:** con [1, 3] da f(x) = x + 3, con [1.0, 3.0] también, con [2.5, 1.0] da
f(x) = 2.5x + 1, y con [2, -3, 1] da f(x) = 2x^2 - 3x + 1

## 5. Reglas que no se pueden cambiar

- **RF1** La lista va de mayor a menor potencia, nunca al revés Si se invierte, el polinomio
  ya no es el mismo
- **RF2** evaluar no redondea El redondeo es cosa de cuando se imprime
- **RF3** a_texto solo arma texto, no calcula nada
- **RF4** La clase nunca usa input ni print Lo que entra viene por parámetros y lo que sale
  es con return El que habla con el usuario es main.py
- **RF5** No se le agregan métodos de derivada ni de integración Esta clase es la función y
  ya
